###
#    for(i=1; i<=N; i++)
# S1:   Y[i] = f(Z[i]);
#
#    for(j=1; j<=N; j++)
# S2:   X[j] = g(Y[j])
#          |
#          V
#    for(i=1; i<=N; i++)
# S1:   Y[i] = f(Z[i]);
# S2:   X[j] = g(Y[j])
#

import islpy as isl
import common

I = isl.UnionSet("[N] -> {S1[i]: 1<=i<=N; S2[j]: 1<=j<=N}")
Sini0 = isl.UnionMap("[N] -> { S1[i] -> [1,i]; S2[j] -> [2,j] }")
Sini  = Sini0.intersect_domain(I) 
print("Initial Schedule:")
print(Sini);

Write  = isl.UnionMap("[N] -> {S1[i] -> Y[i]; S2[j] -> X[j]}").intersect_domain(I) 
Read   = isl.UnionMap("[N] -> {S1[i] -> Z[i]; S2[j] -> Y[j]}").intersect_domain(I) 
Dep    = common.mkDepGraph(Sini, Read, Write)
print("Dependency graph is:")
print(Dep);

Snew = isl.UnionMap("[N] -> {S1[i] -> [i,1]; S2[j] -> [j,2]}").intersect_domain(I)
#Snew = isl.UnionMap("[N] -> {S1[i] -> [1,1]; S2[j] -> [1,2]}").intersect_domain(I)
print("New Schedule:");
print(Snew);

(timesrcsink, is_empty) = common.checkTimeDepsPreserved(Snew, Dep)
print("Time Dependencies (Src -> Sink) On New Schedule:");
print(timesrcsink);
print("Dependencies Respected by New Schedule:")
print(is_empty);
