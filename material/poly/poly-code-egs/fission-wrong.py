###
#    for(p=1; p<=N; p++)
# S1:   Y[p] = f(Z[p]);
# S2:   X[p] = g(Y[p+1])
#            |
#            V
#    for(i=1; i<=N; i++)
# S1:   Y[i] = f(Z[i]);
#
#    for(j=1; j<=N; j++)
# S2:   X[j] = g(Y[j+1])

import islpy as isl
import common

I = isl.UnionSet("[N] -> {S1[p]: 1<=p<=N; S2[p]: 1<=p<=N}")
Sini0 = isl.UnionMap("[N] -> { S1[p] -> [p,1]; S2[p] -> [p,2] }")
Sini  = Sini0.intersect_domain(I) 
print("Initial Schedule:")
print(Sini);

Write  = isl.UnionMap("[N] -> {S1[p] -> Y[p]; S2[p] -> X[p]}").intersect_domain(I) 
Read   = isl.UnionMap("[N] -> {S1[p] -> Z[p]; S2[p] -> Y[p+1]}").intersect_domain(I) 
Dep    = common.mkDepGraph(Sini, Read, Write)
print("Dependency graph is:")
print(Dep);

Snew = isl.UnionMap("[N] -> {S1[i] -> [1,i]; S2[j] -> [2,j]}").intersect_domain(I)
print("New Schedule:");
print(Snew);

(timesrcsink, is_empty) = common.checkTimeDepsPreserved(Snew, Dep)
print("Time Dependencies (Src -> Sink) On New Schedule:");
print(timesrcsink);
print("Dependencies Respected by New Schedule:")
print(is_empty);
