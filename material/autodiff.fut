-- Simple example of forward-mode AD in Futhark.

-- | Mathematical definition of a field.  We wish to differentiate
-- functions whose arguments are fields.
module type field = {
  -- | The field element type.
  type t

  -- | Constructing an element from an integer.
  val i64 : i64 -> t

  val + : t -> t -> t
  val - : t -> t -> t
  val * : t -> t -> t
  val / : t -> t -> t

  -- | Additive identity.
  val zero : t

  -- | Multiplicative identity.
  val one : t

  -- | Additive inverse.
  val negate : t -> t

  -- | Multiplicative inverse.
  val recip : t -> t
}

-- | An ordered field is a field that also admits the usual comparison
-- operators.
module type ordered_field = {
  include field

  val ==: t -> t -> bool
  val <: t -> t -> bool
  val >: t -> t -> bool
  val <=: t -> t -> bool
  val >=: t -> t -> bool
  val !=: t -> t -> bool
}

-- | A convenience parametric module for constructing field modules
-- from the builtin numeric modules like f64 and f64.
module mk_field_from_numeric (F: numeric) : ordered_field with t = F.t = {
  type t = F.t
  let i64 = F.i64
  let (+) = (F.+)
  let (-) = (F.-)
  let (*) = (F.*)
  let (/) = (F./)
  let (==) = (F.==)
  let (<) = (F.<)
  let (>) = (F.>)
  let (<=) = (F.<=)
  let (>=) = (F.>=)
  let (!=) = (F.!=)

  let zero = F.i64 0
  let one = F.i64 1
  let negate x = zero - x
  let recip x = one / x
}

-- | The module type of fields of dual numbers.  Supports the usual
-- field operations, as well as extracting the "primal" (normal) and
-- "tangent" (differentiated) components of a computation.
module type dual_field = {
  -- The element type of the underlying field (the components of the
  -- dual numbers).
  type underlying

  -- | We include all the operations required by ordered fields.  The
  -- 't' will be a dual number.
  include ordered_field

  -- | The primal of a dual number if the normal result.
  val primal : t -> underlying

  -- | The tangent is, well, the tangent..
  val tangent : t -> underlying

  -- | Construct a dual number with tangent zero.
  val dual0 : underlying -> t

  -- | Construct a dual number with tangent one.
  val dual1 : underlying -> t
}

-- | Given an ordered field, construct a dual number field.  We keep
-- the actual representation of the dual numbers abstract.
module mk_dual (F: ordered_field) : (dual_field with underlying = F.t) = {
  type underlying = F.t
  -- We represent a dual number as a pair of the "primal" and
  -- "tangent" parts.
  type t = (underlying, underlying)
  let primal ((x, _) : t) = x
  let tangent ((_, x') : t) = x'
  let dual0 x : t = (x, F.i64 0)
  let dual1 x : t = (x, F.i64 1)

  -- A constant has tangent zero.
  let i64 x = dual0 (F.i64 x)
  let zero = i64 0
  let one = i64 1

  -- Negation is defined in the obvious way.
  let negate (x,x') = (F.negate x, F.negate x')

  -- The reciprocal is a little more tricky, but you can look up the
  -- reciprocal rule in a calculus textbook (or more realistically, on
  -- Wikipedia).
  let recip (x,x') = (F.recip x, F.(negate (x'/(x*x))))

  -- Then we get to the actual arithmetic operations.  These are also
  -- as you'd expect to find in a textbook.  We define subtraction and
  -- division via the inverse elements, so we have fewer things
  -- written from scratch.
  let (x,x') + (y,y') = F.((x + y, x' + y'))
  let (x,x') * (y,y') = F.((x * y, x' * y + x * y'))
  let x - y = x + negate y
  let x / y = x * recip y

  -- Comparisons are straightforward and use only the primal parts.
  -- Since we produce booleans here, the result has no tangent.
  let (x,_) == (y,_) = F.(x == y)
  let (x,_) < (y,_) = F.(x < y)
  let (x,_) > (y,_) = F.(x > y)
  let (x,_) <= (y,_) = F.(x <= y)
  let (x,_) >= (y,_) = F.(x >= y)
  let (x,_) != (y,_) = F.(x != y)
}

-- | To show off forward-mode AD, we define various functions
-- parameterised over the field representation.  This lets us evaluate
-- them using normal numbers or dual numbers.  In Haskell we'd use
-- type classes for this, but in Futhark and other ML languages, we
-- define a parametric module.
module mk_example (F: ordered_field) = {
  let test (x: F.t) (y: F.t) =
    F.((x*x) + (x*y))

  let f3 (x: [3]F.t) =
    F.(i64 3*(x[0]*x[0]+x[1]*x[2]))

  -- We can also use control flow - note that this function is not
  -- differentiable for x=0.
  let abs (x: F.t) =
    if F.(x < i64 0)
    then F.negate x
    else x

  -- Exponentiation by repeated multiplication.
  let pow (x: F.t) (k: i64) =
    loop res = F.i64 1 for _i < k do
      F.(res * x)

  -- Newton-Rhapson iteration.
  let sqrt (x: F.t) =
    let difference = F.(i64 1 / i64 1000)
    in loop guess = F.i64 1
       while F.(abs(guess * guess - x) >= difference) do
         F.((x/guess + guess)/(i64 2))

  let sum = reduce (F.+) F.zero
  let product = reduce (F.*) F.one

  let alternate_sum (xs: []F.t) =
    let f i x =
      if i % 2 == 0 then x else F.negate x
    in sum (map2 f (indices xs) xs)

  let alternate_product (xs: []F.t) =
    let f i x =
      if i % 2 == 0 then x else F.negate x
    in product (map2 f (indices xs) xs)

  let avg [n] (xs: [n]F.t) =
    F.(sum xs / i64 n)

  -- | Evaluate a polynomial, giving the coefficients (ranging from
  -- lowest to highest order) and the variable.
  let polynomial [k] (coeffs: [k]F.t) (x: F.t) =
    let term a i =
      F.(a * pow x i)
    in sum (map2 term coeffs (iota k))

  -- | The L2 norm, which is a fancy word for Euclidean distance.
  let L2 A B =
    sqrt (sum (map2 (\a b -> F.(pow (a-b) 2)) A B))

  -- | Compute the distance from a polynomial approximation of a
  -- function to the observed values of that function (ys), at certain
  -- inputs (xs).  This is a cost function that must be minimised with
  -- respect to 'coeffs' to provide a good approximation.
  let polynomial_badness [k] [n] (coeffs: [k]F.t) (xs: [n]F.t) (ys: [n]F.t) =
    L2 (map (\x -> polynomial coeffs x) xs) ys
}

-- Instantiating the modules, first with ordinary numbers.
module f64_field = mk_field_from_numeric f64
module example_f64 = mk_example f64_field

-- And then with dual numbers.
module dual_f64 = mk_dual f64_field
module example_dual_f64 = mk_example dual_f64

-- Now we can experiment, e.g to compute the two derivatives of the
-- 'test' function at some point:
let test' x y =
  let a = example_dual_f64.test (dual_f64.dual1 x) (dual_f64.dual0 y)
  let b = example_dual_f64.test (dual_f64.dual0 x) (dual_f64.dual1 y)
  in (dual_f64.tangent a, dual_f64.tangent b)
-- Note that we have to compute the function once for every parameter
-- that we wish to take the (partial) derivative for.

-- Or the derivative of pow and sqrt:
let pow' x k =
  dual_f64.tangent (example_dual_f64.pow (dual_f64.dual1 x) k)
let sqrt' x =
  dual_f64.tangent (example_dual_f64.sqrt (dual_f64.dual1 x))
-- Check for yourself whether they match the analytical results you
-- were taught in school.

-- For functions that take arrays as arguments, we define a function
-- such that 'dual1_at i xs' produces an array of dual numbers that
-- have tangent of 0 everywhere, except at element 'i', where it has
-- 1.
let dual1_at i xs =
  let f j x =
    if i == j then dual_f64.dual1 x else dual_f64.dual0 x
  in map2 f (indices xs) xs

-- We can then write a function for computing the Jacobian - all
-- partial derivatives - of a function that takes 'n' inputs and
-- produces 'm' outputs.
let jacobian [n][m] (f: [n]dual_f64.t -> [m]dual_f64.t) (xs: [n]f64) : [n][m]f64 =
  tabulate n (\i -> map dual_f64.tangent (f (dual1_at i xs)))

-- As a small convenience, a special case for functions that return
-- only one value.
let jacobian1 [n] (f: [n]dual_f64.t -> dual_f64.t) (xs: [n]f64) : [n]f64 =
  (jacobian (\x -> [f x]) xs)[:,0]

-- Now we can define a function for computing how close a
-- polynomial-based approximation to f64.sin with gets to the true
-- values ("badness"), as well as the gradients for the badness.  This
-- can be used to drive a search procedure that calibrates the
-- gradients.
let sin_badness coeffs xs =
  let ys = map f64.sin xs
  let got = map (\x -> example_f64.polynomial coeffs x) xs
  in (got,
      jacobian1 (\coeffs' ->
                   example_dual_f64.polynomial_badness
                   coeffs'
                   (map dual_f64.dual0 xs)
                   (map dual_f64.dual0 ys))
                coeffs)
