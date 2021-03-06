# Project suggestions

These projects are intentionally open-ended.  They are intended as an
opportunity for you to showcase your mastery of the learning goals:

* Parallel algorithmic reasoning.

* Parallel cost models.

* Judging the suitability of the language/tool for the problem at
  hand.

* Applied data-parallel programming.

This means that you are free to diverge from the project descriptions
below, or come up with your own ideas, as long as they provide a
context in which you can demonstrate the course contents.

You are *not* judged on whether e.g. Futhark or ISPC or whatever
language you choose happens to be a good fit or run particularly fast
for whatever problem you end up picking, but you *are* judged on how
you evaluate its suitability.

## Parallelising multiple precision arithmetic

Machines tend to support only numbers of some fixed precision, such as
32 or 64 bits.  Larger numbers must be implemented in software.  Some
domains, such as cryptography, involved numbers that are much larger
than what is directly supported by machines.  While there is perhaps
not much need for parallelising 128-bit arithmetic, operations on much
larger numbers may be worth parallelising.  For example, a scan can be
used to implement addition (see [this Blelloch
paper](material/prefix-sums-and-their-applications.pdf)).

This project is about implementing, in Futhark, a small library for
multiple precision integer arithmetic.  The goal is to handle integers
of any *fixed* user-provided size (that is, not full
arbitrary-precision).  Addition, subtraction, and multiplication
should be straightforward.  Division is likely also doable.  Depending
on time and interest, you can move on from there.

For inspiration and performance comparison:

* [The CGBN library for CUDA](https://github.com/NVlabs/CGBN)

* [The GNU Multiple Precision Arithmetic Library](https://gmplib.org/)

## Porting a Parboil benchmark to a parallel language

[Parboil](http://impact.crhc.illinois.edu/parboil/parboil.aspx) is a
suite of benchmarks that is used when presenting new research into
compilers or parallel programming.  This project is about picking one
of the benchmarks and porting it to a parallel language covered in
class (I prefer Futhark, but if you want to use `ispc` or Parallel
Haskell, that's fine too).  For Futhark, [we already have
implementations of `histo`, `mri-q`, `sgemm`, `stencil`, and
`tpacf`](https://github.com/diku-dk/futhark-benchmarks/tree/master/parboil),
so we are mostly interested in the remaining ones.  In particular, we
have an interest in the `lbm` benchmark.

## Fast Radix-Sort in Futhark

[See project reseources here, including a short document introducing the project, namely Project-Sorting.pdf](some-suggested-projects/fast-radix-futhark)

[The Cub Library and a template program using CUB's radix sort are provided here](some-suggested-projects/)

## Flattening a Batch of Rank-Search-k Problems

[See project description here](some-suggested-projects/rank-search-k/Project-RankSearch-k.pdf)

[The Cub Library and a template program using CUB's radix sort are provided here](some-suggested-projects/)

## Compiler Enhancements to Reverse AD

[See project description here](some-suggested-projects/compiler-ad/Compiler-AD-Topics.pdf)

## Porting PBBS benchmarks

The [Problem Based Benchmark
Suite](https://cmuparlay.github.io/pbbsbench/) is a collection of
benchmark programs written in parallel C++.  We are interested in
porting them to a high-level parallel language (e.g. Futhark).  Some
of the benchmarks are relatively trivial; others are more difficult.
It might be a good idea for a project to combine a trivial benchmark
with a more complex one.  The [list of benchmarks is
here](https://cmuparlay.github.io/pbbsbench/benchmarks/index.html).
The ones listed as *Basic Building Blocks* are all pretty
straightforward.  Look at the others and pick whatever looks
interesting (but talk to us first - some, e.g. rayCast, involve no
interesting parallelism, and so are not a good DPP project).
