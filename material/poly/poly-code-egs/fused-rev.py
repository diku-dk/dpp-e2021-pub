###
#    for(i=0; i<=N; i++)
# S1:   Y[N-i] = f(Z[i]);
#
#    for(j=0; j<=N; j++)
# S2:   X[j] = g(Y[j])
#            |
#            V
#    for(p=0; p<=N; p++) {
# S1:   Y[p] = Z[N-p];
# S2:   X[p] = Y[p];
#    }
# A[i] == A[0,i]
# B[i] == A[1,i]
# C[i] == A[2,i]

import islpy as isl
import common

I = isl.UnionSet("[N] -> {S1[i]: 0<=i<=N; S2[j]: 0<=j<=N}")
Sini = isl.UnionMap("[N] -> {S1[i] -> [1,i]; S2[j] -> [2,j]}").intersect_domain(I)
print("Initial Schedule:")
print(Sini);

Write  = isl.UnionMap("[N] -> {S1[i] -> Y[N-i]; S2[j] -> X[j]}").intersect_domain(I)
Read   = isl.UnionMap("[N] -> {S1[i] -> Z[i];   S2[j] -> Y[j]}").intersect_domain(I)
Dep    = common.mkDepGraph(Sini, Read, Write)
print("Dependency graph is:")
print(Dep);

Snew = isl.UnionMap("[N] -> {S1[p] -> [N-p,1]; S2[j] -> [j,2]}").intersect_domain(I)
print("New Schedule:");
print(Snew);

(timesrcsink, is_empty) = common.checkTimeDepsPreserved(Snew, Dep)
print("Time Dependencies (Src -> Sink) On New Schedule:");
print(timesrcsink);
print("Dependencies Respected by New Schedule:")
print(is_empty);
