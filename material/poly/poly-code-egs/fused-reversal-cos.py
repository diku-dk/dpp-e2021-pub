###
#    for(i=0; i<N; i++)
# S[1]:   B[i] = f(A[i]);
#
#    for(j=0; j<N; j++)
# S[2]:   C[N-1-j] = g(B[j])

# A[i] == A[0,i]
# B[i] == A[1,i]
# C[i] == A[2,i]

import islpy as isl
import common

Sini   = isl.UnionMap("[N] -> {S1[i] -> [1,i]: 0<=i<N; S2[j] -> [2,j]: 0<=j<N}")
print("Initial Schedule:")
print(Sini);

Write  = isl.UnionMap("[N] -> {S1[i] -> B[i]: 0<=i<N; S2[j] -> C[N-1-j]: 0<=j<N}")
Read   = isl.UnionMap("[N] -> {S1[i] -> A[i]: 0<=i<N; S2[j] -> B[j]    : 0<=j<N}")
Dep    = common.mkDepGraph(Sini, Read, Write)
print("Dependency graph is:")
print(Dep);

Snew = isl.UnionMap("[N] -> {S1[i] -> [i,1]: 0<=i<N; S2[j] -> [j,2]: 0<=j<N}")
print("New Schedule:");
print(Snew);

(timesrcsink, is_empty) = common.checkTimeDepsPreserved(Snew, Dep)
print("Time Dependencies (Src -> Sink) On New Schedule:");
print(timesrcsink);
print("Dependencies Respected by New Schedule:")
print(is_empty);
