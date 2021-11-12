import islpy as isl

#############
#   for(i=0; i<N; i++) {
#     for(j=0; j<N-i; j++) {
#F:     a[i+j] = f(a[i+j]);
#     }
#   }
#
#   for(i=0; i<N; i++) {
#S:   x[i] = g(a[i]);
#   }

W1 = isl.Map("[N] -> { F[i,j]->a[i+j]: 0<=i<N and 0 <= j < N-i }")
R2 = isl.Map("[N] -> { S[i] -> a[i]: 0 <= i < N}")
R  = isl.Map.apply_range(R2, isl.Map.reverse(W1))
LstWrite = isl.Map.lexmax(R)
print("Last Write:");
print(LstWrite);
