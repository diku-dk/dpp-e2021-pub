# Bootstrap Futhark exercises

As a warmup to the course, ensure that you are able to compile, run,
and benchmark Futhark programs, either on your own machine or on
[DIKUs GPU cluster](README.md#practical-information).

The following exercises serve as a simple introduction to Futhark
programming.  They should be solvable using material from the Monday
lecture and [the Futhark book](https://futhark-book.readthedocs.io).

## Reimplement library functions

Implement the following Futhark utility functions:

```
let rotate [n] 't (r: i64) (xs: [n]t) : [n]t =
  ...

let transpose [n] [m] 't (xss: [n][m]t) : [m][n]t =
  ...

let concat [n] [m] 't (xs: [n]t) (ys: [m]t) : []t =
  ...

```

This is doable with `map`s (possibly nested) and explicit array
indexing.  [Make sure to also write
tests](https://futhark-book.readthedocs.io/en/latest/practical-matters.html#testing-and-debugging).
How fast do they run using the `opencl` backend compared to the `c`
backend?

## Sequential looping

Use `loop` to implement a function for counting how many `1` bits are
set in an `i32` value.  Test your results against the built-in
`i32.popc`.

## Implement 1D smoothing

A one-dimensional array `xs` can be *smoothed* by, for every index
`xs[i]`, recomputing it as `(x[i-1] + x[i] + x[i+1])/3`.  This
pattern, where we update a cell in a grid based on its neighbours, is
called a *stencil*.  Implement this one-dimensional smoothing in
Futhark.

What should you do for elements at the edge?

## Some linear algebra

Implement the following functions using `map`, `map2`, `reduce`, and
`transpose`.

```
-- Multiply every element of vector with a scalar.
let vec_scale [n] (s: f32) (xs: [n]f32) : [n]f32 =
  ...

-- Elementwise addition of vectors.
let vec_add [n] (xs: [n]f32) (xs: [n]f32) : [n]f32 =
  ...

-- Dot product.
let dotprod [n] (xs: [n]f32) (ys: [n]f32) : f32 =
  ...

-- Matrix multiplication (the dot product of the rows of 'xss'
-- with the columns of 'yss').
let matmul [n][m][p] (xss: [n][p]f32) (yss: [p][m]f32) : [n][m]f32 =
  ...
```

You can write all of these without any explicit indexing.

## Implement Game of Life

The [Game of
Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a
two-dimensional stencil.  Implement it in Futhark.
