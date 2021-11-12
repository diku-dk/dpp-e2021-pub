###
#     float X[N][N];
#     for(int i=1; i<N; i++) {
#       for(int j=1; j < min(i+2, N); j++) {
# S1:     X[i][j] = X[i-1][j] + X[i][j-1];
#       }
#     }
#                   |
# Change of variables: p <- i+j,  q <- j
#                   |
#                   V
#     for(int p=2; p < 2*N-1; p++) {
#       int up_bd = ((p+2)/2) + (p%2);
#       for(int q=max(1,p-N+1); q<min(up_bd,N); q++) {
# S1:     X[p-q][q] = X[p-q-1][q] + X[p-q][q-1];
#       }
#     }

import islpy as isl
import common

I = isl.UnionSet("[N] -> {S1[i,j]: 1<=i<N and 1<=j<min(i+2, N)}")
Sini0 = isl.UnionMap("[N] -> { S1[i,j] -> [i,j] }")
Sini  = Sini0.intersect_domain(I) 
print("Initial Schedule:")
print(Sini);
print(I);

Write  = isl.UnionMap("[N] -> {S1[i,j] -> X[i,j]}").intersect_domain(I) 
Read   = isl.UnionMap("[N] -> {S1[i,j] -> X[i-1,j]; S1[i,j] -> X[i,j-1]}").intersect_domain(I) 
Dep    = common.mkDepGraph(Sini, Read, Write)
print("Dependency graph is:")
print(Dep);

#Inew = isl.UnionSet("[N] -> {S1[p,q]: 2<=p<2*N-1 and max(1,p-N+1)<=q<min((p+2)/2 + (p mod 2), N)}")
Snew = isl.UnionMap("[N] -> {S1[x,q] -> [x+q,q]}").intersect_domain(I)
#Snew = isl.UnionMap("[N] -> {S1[x,q] -> [x+q,1]}").intersect_domain(Inew)

print("New Schedule:");
print(Snew);

#WriteNew  = isl.UnionMap("[N] -> {S1[p,q] -> X[p-q,q]}").intersect_domain(Inew) 
#ReadNew   = isl.UnionMap("[N] -> {S1[p,q] -> X[p-q-1,q]; S1[p,q] -> X[p-q,q-1]}").intersect_domain(Inew) 
#DepNew       = common.mkDepGraph(Snew, ReadNew, WriteNew)
#print("Dependency Graph New is:")
#print(DepNew);

(timesrcsink, is_empty) = common.checkTimeDepsPreserved(Snew, Dep)
print("Time Dependencies (Src -> Sink) On New Schedule:");
print(timesrcsink);
print("Dependencies Respected by New Schedule:")
print(is_empty);
