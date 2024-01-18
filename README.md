# Data Parallel Programming (DPP), Block 2 2021

DPP is structured around five weeks with lectures and lab sessions
on Monday and Wednesday, followed by a final project to be
presented orally at the exam.  Throughout the course, you will hand in
four weekly assignments.  These *weeklies* count for 40\% of the
grade, while the exam counts for 60\%.

The teachers are **Cosmin Oancea** and **Troels Henriksen**.

All lectures and lab sessions will be delivered in English.  The
assignments and projects will be posted in English, and while you can
chose to hand in solutions in either English or Danish, English is
preferred.

All course material is distributed via this GitHub page.  Assignment
handin is still on Absalon.  There is no mandated textbook for the
course - you will be assigned reading material from papers and such.

## Course schedule

[Course Catalog Web Page](https://kurser.ku.dk/course/ndak21006u/2021-2022)

### Lectures (zoom links will be posted on Absalon):

* Monday    13:00 - 15:00 (weeks 47-51, 1-3	in øv - Kursussal 3, Universitetsparken 15, Zoo)
* Wednesday 10:00 - 12:00 (weeks 47-51, 1-3	in aud - Aud 03 AKB, Universitetsparken 13)

### Labs:

* Wednesday 13:00 - 17:00 (weeks 47-51, 1-3, in øv - Auditorium Syd, Nørre Alle 51, NEXS)

[Location of lectures and labs](https://skema.ku.dk/tt/tt.asp?SDB=ku2122&language=EN&folder=Reporting&style=textspreadsheet&type=student+set&idtype=id&id=167421&weeks=1-53&days=1-7&periods=1-68&width=0&height=0&template=SWSCUST+student+set+textspreadsheet)

The current plan is that everybody will have a physical place
at the lecture and lab. Unless we are forced to move to virtual
teaching, the lectures and labs will not be recorded, so please
plan to attend (albeit, if there is a strong request, we may
zoom them online).


This course schedule is tentative and will be updated as we go along.
**The schedule below will become the correct one as you enter the
week when the course starts.**

The lab sessions are aimed at providing help for the weeklies and
group project.  Do not assume you can solve them without showing
up to the lab sessions.

[Zoom link for lectures](https://ucph-ku.zoom.us/j/67002083301?pwd=SjdGdlZmRllXMEd1VVcxU0p6QlR1Zz09)

### Lecture plan

| Date | Time | Topic | Material |
| --- | --- | --- | --- |
| 22/11 | 13:00-15:00 | [Intro, deterministic parallelism, data parallelism, Futhark](slides/L1-determ-prog.pdf) | [Parallel Programming in Futhark](https://futhark-book.readthedocs.io/en/latest/), sections 1-4, [Futhark exercises](bootstrap-exercises.md) | |
| 24/11 | 10:00-12:00 | [Cost models, advanced Futhark](slides/L2-advanced-futhark-cost-models.pdf) | [Guy Blelloch: Programming Parallel Algorithms](material/blelloch-programming-parallel-algorithms.pdf), [Prefix Sums and Their Applications](material/prefix-sums-and-their-applications.pdf), [A Provable Time and Space Efficient Implementation of NESL](material/a-provable-time-and-space-efficient-implementation-of-nesl.pdf) |
| 24/11 | 13:00-17:00 | Lab ([**Assignment 1 handout**](weekly-1/)) | |
| 29/11 | 13:00-15:00 | [List homomorphisms](slides/L3-list-homomorphisms.pdf) | [The Third Homomorphism Theorem](material/algorithms/lhomo-third-theorem.pdf), [Construction of List Homomorphisms by Tupling and Fusion](material/algorithms/lhomo-tupling.pdf) |
| 01/12 | 10:00-12:00 | [Vector programming with ISPC](slides/L4-ispc.pdf) | [ispc: A SPMD Compiler for High-Performance CPU Programming](material/ispc_inpar_2012.pdf) | |
| 01/12 | 13:00-17:00 | Lab ([**Assignment 2 handout**](weekly-2/)) | |
| 06/12 | 13:00-15:00 | [Full/irregular flattening](slides/L5-irreg-flattening.pdf) | [PMPH lecture notes, Chapter 4](http://hjemmesider.diku.dk/~zgh600/Publications/lecture-notes-pmph.pdf), [Transforming High-Level Data-Parallel Programs into Vector Operations](material/flattening/NeslFlatTechPaper.pdf), [Harnessing the Multicores: Nested Data Parallelism in Haskell](material/flattening/harnessing-multicores.pdf) (not easy to read)|
| 08/12 | 10:00-12:00 | [Full/irregular flattening](slides/L5-irreg-flattening.pdf) | [PMPH lecture notes, Chapter 4](http://hjemmesider.diku.dk/~zgh600/Publications/lecture-notes-pmph.pdf), [Transforming High-Level Data-Parallel Programs into Vector Operations](material/flattening/NeslFlatTechPaper.pdf), [Harnessing the Multicores: Nested Data Parallelism in Haskell](material/flattening/harnessing-multicores.pdf) (not easy to read)|
| 08/12 | 13:00-17:00 | Lab ([**Assignment 3 handout**](weekly-3/)) | |
| 13/12 | 13:00-15:00 | [Polyhedral Analysis](slides/L7-polyhedral.pdf) | [PMPH Dependence Analysis](material/poly/L5-LoopParI.pdf); [Sven Verdoolaege: Presburger Formulas and Polyhedral Compilation (tutorial)](material/poly/polycomp-tutorial.pdf); [Sven Verdoolaege: Presburger Sets and Relations: from High-Level Modelling to Low-Level Implementation (slides)](material/poly/poly-in-detail.pdf), [Code Examples](material/poly/poly-code-egs/) |
| 15/12 | 10:00-12:00 | [Regular and incremental flattening](slides/L8-regular-flattening.pdf) | [Futhark: Purely Functional GPU-Programming with Nested Parallelism and In-Place Array Updates](https://futhark-lang.org/publications/pldi17.pdf),  [Incremental Flattening for Nested Data Parallelism](https://futhark-lang.org/publications/ppopp19.pdf) (particularly the latter) |
| 15/12 | 13:00-17:00 | Lab ([**Assignment 4 handout**](weekly-4)) | |
| 20/12 | 13:00-15:00 | [Data-parallel automatic differentiation](slides/L9-AD.pdf) | [Automatic Differentiation in Machine Learning: a Survey, Baydin et. al.](material/automatic_differentiation_in_ml_baydin.pdf), [autodiff.fut](material/autodiff.fut) |
| 22/12 | 10:00-12:00 | [Data-parallel automatic differentiation](slides/L9-AD.pdf) | same material as previous lecture |
| 22/12 | 13:00-15:00 | Lab (with project proposals) | |

After New Years, *maybe* there will be no lectures (we are still thinking on it),
but labs will still be held to help with the group project.

| Date | Time |
| ---  | ---  |
| 05/1 | 13:00-17:00 |
| 12/1 | 13:00-17:00 |
| 19/1 | 13:00-17:00 |

## Weekly assignments

The weekly assignments are **mandatory**, must be solved
**individually**, and make up 40% of your final grade.  Submission is
on Absalon.

You will receive feedback a week after the handin deadline (at the
latest).  You then have another week to prepare a resubmission.  That
is, **the resubmission deadline is two weeks after the original handin
deadline**.

The assignment text and handouts will be linked in the schedule above.

## Group project and exam

The final project, along with the exam as a whole, contributes 60% of
your grade, and is done in groups of 1-3 people (although working
alone is strongly discouraged).  We have [a list of project
suggestions](project-suggestions.md), but you are free to suggest your
own (but please talk with us first).  Since the time to work on the
project is rather limited, and there is no possibility of
resubmission, you should ask for help early and often if you are
having trouble making progress.  **The project should be handed in via
Absalon on Friday the 21st of January**.  Send an email if you have
trouble meeting this deadline.

Most of the projects are about writing some parallel program, along
with a report describing the main points and challenges of the
problem.  The exam format is a group presentation followed by
individual questions about both your project **and anything else in
the curriculum**.  Each group prepares a common presentation with
slides, and each member of the group presents non-overlapping parts of
the presentation for about 10 min (or less). Then each member of the
group will answer individual questions for about 10 min.

## Practical information

You may find it useful to make use of DIKUs GPU machines in your work.
You log in by first SSHing to the bastion server
`ssh-diku-apl.science.ku.dk` using your KU license plate (`abc123`) as
the user name, and then SSHing on to one of the GPU machines.  Despite
their names, they each have two multi-core CPUs and plenty of RAM as
well.

  * `gpu01-diku-apl`, `gpu02-diku-apl`, `gpu03-diku-apl` have dual GTX
    780 Ti GPUs.

  * `phi-diku-apl` has a K40 GPU.

  * `gpu04-diku-apl` has a GTX 2080 Ti GPU (by far the fastest).

All machines should have all the software installed you need.  If you
are missing something, [contact Troels](mailto:athas@sigkill.dk).  The
machines have a shared home directory (which is very slow), *except*
`gpu01-diku-apl`, which has its own home directory (which is a little
faster).

### SSH setup

To enable more convenient access to the servers, you can add entries
to your `~/.ssh/config` file.  Example:

```
Host gpu04-diku-apl
HostName gpu04-diku-apl
ProxyJump mzd885@ssh-diku-apl.science.ku.dk
User mzd885
ForwardAgent yes
```

Replace `gpu04-diku-apl` with the server you want and `mzd885` with
your KU license plate (unless you are fortunate enough to be Troels).
After this you can use `ssh gpu04-diku-apl` to log in directly
(although you will still need to enter your password twice).

The real win is that now you can use
[sshfs](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)
to mount the remote file system on your local machine:

```
$ mkdir remote
$ sshfs gpu04-diku-apl: remote
```

### GPU setup

For CUDA to work, you may need to add the following to your `$HOME/.bash_profile`:

```bash
CUDA_DIR=/usr/local/cuda
export PATH=$CUDA_DIR/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_DIR/lib64:$LD_LIBRARY_PATH
export LIBRARY_PATH=$LD_LIBRARY_PATH:$LIBRARY_PATH
export CPLUS_INCLUDE_PATH=$CUDA_DIR/include:$CPLUS_INCLUDE_PATH
export C_INCLUDE_PATH=$CUDA_DIR/include:$C_INCLUDE_PATH
```

### Compiling the Futhark compiler on the GPU servers

**These instructions are only for when you need to compile Haskell
programs (such as the Futhark compiler itself) on the servers, not if
you just want to compile Futhark programs.  Most students will not
need this.**

The network file system used by SCIENCE-IT on the GPU servers has a
bug which makes the `open()` syscall not set the executable bit
properly on new files for some users.  It can be set subsequently with
the `chmod()` syscall, but the `ld.gold` linker that GHC uses by
default quite reasonably expects that basic system calls work.  The
end result is that `ld.gold` produces non-executable binaries, and
this makes GHC malfunction.  The suggested workaround is to
transparently replace `ld.gold` with the older linker `ld`, which
happens to implement file creation by separately calling `chmod()`.
You do this by ensuring `$HOME/.local/bin` is first on your `PATH`,
and then symlinking:

```
$ ln -s `which ld` $HOME/.local/bin/ld.gold
```

This will make GHC (and all other tools) use `ld` instead of `ld.gold`.

Furthermore, for SCIENCE-IT reasons, you don't actually own your home directory
on those machines, and this tends to confuse some software. Therefore, you
should manually create a stack root before proceeding with compilation
of the Futhark compiler:

```
$ mkdir $HOME/.stack
```

* **Yes**, it is absolutely ridiculous that basic filesystem
  operations don't work in TYOOL 2020.  Blame whichever buggy NFS
  servers is actually hosting these home directories.

* **No**, it is unlikely that this will ever be fixed.  We reported
  this to SCIENCE-IT a year ago, and the issue can be demonstrated by
  a tiny C program, but have not yet heard anything back.

## Other resources

You are not expected to read/watch the following unless otherwise
noted, but they contain useful and interesting background information.

* [The Futhark User's Guide](https://futhark.readthedocs.io), in
  particular [Futhark Compared to Other Functional
  Languages](https://futhark.readthedocs.io/en/latest/versus-other-languages.html)

* [Troels' PhD thesis on the Futhark compiler](https://futhark-lang.org/publications/troels-henriksen-phd-thesis.pdf)

* [A library of parallel algorithms in NESL](http://www.cs.cmu.edu/~scandal/nesl/algorithms.html)

* [Functional Parallel Algorithms by Guy Blelloch](https://vimeo.com/showcase/1468571/video/16541324)

* ["Performance Matters" by Emery Berger](https://www.youtube.com/watch?v=r-TLSBdHe1A)

* [The story of `ispc`](https://pharr.org/matt/blog/2018/04/18/ispc-origins.html) (you can skip the stuff about office politics, although it might ultimately be the most valuable part of the story)

* [Scientific Benchmarking of Parallel Computing
  Systems](https://htor.inf.ethz.ch/publications/img/hoefler-scientific-benchmarking.pdf)
  (we benchmark much simpler systems and don't expect anywhere near
  this much detail, but it's useful to have thought about it)
