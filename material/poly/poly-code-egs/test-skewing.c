#include<stdlib.h>
#include<stdio.h>
#include<math.h>

#define min(x,y) (((x) < (y)) ? (x) : (y))
#define max(x,y) (((x) < (y)) ? (y) : (x))

void origLoop(const int N, int X[N][N]) {
    for(int i=1; i<N; i++) {
        for(int j=1; j < min(i+2, N); j++) {
            X[i][j] = X[i-1][j] + X[i][j-1];
        }
    }
}

void skewLoop(const int N, int X[N][N]) {
    for(int p=2; p < 2*N-1; p++) {
        int up_bd = ((p+2)/2) + (p%2);
        for(int q = max(1,p-N+1); q < min(up_bd, N); q++) {
            //if(p-q > 0 && p-q < N)
            X[p-q][q] = X[p-q-1][q] + X[p-q][q-1];
        }
    }
}


int main() {
    const int N = 5;
    int A[5][5] = { {1,2,3,4,5}
                  , {6,7,8,9,10}
                  , {11,12,13,14,15}
                  , {16,17,18,19,20}
                  , {21,22,23,24,25}
                  };
    int B[5][5];
    int C[5][5];

    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            B[i][j] = A[i][j];
            C[i][j] = A[i][j];
        }
    }
    origLoop(N, B);
    skewLoop(N, C);

    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(B[i][j] != C[i][j]) {
                printf("Invalid at index (%d,%d): %d, %d\n"
                      , i, j, B[i][j], C[i][j]
                      );
                exit(1);
            }
        }
    }
    printf("VALID\n");
    return 1;
}
