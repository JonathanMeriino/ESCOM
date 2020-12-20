#include <stdio.h>
#include <stdlib.h>

int **crearMatriz(int M, int N);
void destruirMatriz(int **mat, int M);
void imprimirMatriz(int **mat, int M, int N);

int main(int argc, char *argv[])
{
	int **matriz= NULL;
	int M= 5, N=5;
	
	matriz= crearMatriz(M, N);	
	imprimirMatriz(matriz, M, N);	
	
	destruirMatriz(matriz, M);
	matriz= NULL;
	
	return 0;
}

int **crearMatriz(int M, int N)
{
	int **mat= NULL;
	int i=0, j=0;
	
	mat= (int **) malloc(M*sizeof(int *));
	
	for (i=0; i<M; i++)
	   {
	   	  mat[i]= (int *) malloc(N*sizeof(int));
	   	  
	   	  for (j=0; j<N; j++)
	   	     mat[i][j]= i*j;	// int
	   }
	   
	return(mat);
}

void destruirMatriz(int **mat, int M)
{
	int i=0;
	
	for (i=0; i<M; i++)
	   free(mat[i]);
	   
	free(mat);
	
	//mat= NULL;
}

void imprimirMatriz(int **mat, int M, int N)
{
	int i=0, j=0;
	
	for (i=0; i<M; i++)
	   {
	   	 for (j=0; j<N; j++)
	   	    printf("%d\t", mat[i][j]);
	   	    
	   	 printf("\n");
	   }
}

