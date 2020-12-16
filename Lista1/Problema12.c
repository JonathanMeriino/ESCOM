#include<stdio.h>
#include<stdlib.h>

void main() {
  float **matrizA= NULL, **matrizB= NULL, **matrizC= NULL;
  int M= 3, N= 3;
    matrizA= crearMatriz(M, N);
    matrizB= crearMatriz(M, N);
    matrizC= crearMatriz(M, N);
    sumarMatrices(matrizC, matrizA, matrizB);
    multiplicarMatrices(matrizC, matrizA, matrizB);
    estruirMatriz(matrizC);
    destruirMatriz(matrizB);
    destruirMatriz(matrizA);
}
float **crearMatriz(int M, int N) {
  float **matrix= NULL;
  int i=0, j=0;
    matriz= (float **) malloc(M*sizeof(float *));
      for (i=0; i<M; i++)
        matrix[i]= (float *) malloc(N*sizeof(float *));
      for (i=0; i<M; i++)
        for (j=0; j<N; j++)
            matrix[i][j]= i*j;
      return(matrix);
}
void destruirMatriz(float **matrix, int M){
  int i=0;
    for (i=0; i<M; i++)
        free(matrix[i]);
    free(matrix);
}
void sumarMatrices(float **mZ, float **mX, float **mY, int M, int N){
  int i=0, j=0;
    if (mX==NULL || mY==NULL || mZ==NULL)
      return;
    for (i=0; i<M; i++)
      for (j=0; j<N; j++)
          mZ[i][j]= mX[i][j] + mY[i][j];
}
void multiplicarMatrices(float **mZ, float **mX, float **mY,int M, int N, int L){
  int i=0, j=0, k=0;
  if (mX==NULL || mY==NULL || mZ==NULL)
    return;
  for (i=0; i<M; i++)
     {
       for (j=0; j<N; j++)
          {
            mZ[i][j]= 0;
            for (k=0; k<L; k++)
              mZ[i][j] += mX[i][k] * mY[k][j];
          }
      }
}
