#include <stdio.h>
#include <stdlib.h>

int ***crearVolumen(int L, int M, int N);
void imprimirVolumen(int ***vol, int L, int M, int N);
void destruirVolumen(int ***vol, int L, int M);
void destruirVolumenSegura(int ****vol, int L, int M);

int main(int argc, char *argv[]) 
{
	int ***volumen= NULL;
	int L= 3, M= 4, N= 5;
	
	volumen= crearVolumen(L, M, N);
	imprimirVolumen(volumen, L, M, N);
	//destruirVolumen(volumen, L, M);
	destruirVolumenSegura(&volumen, L, M);
	
	printf("volumen= %X\n", volumen);
	
	return 0;
}

int ***crearVolumen(int L, int M, int N)
{
	int ***vol= NULL;
	int i=0, j=0, k=0;
	
	vol= (int ***) malloc(L*sizeof(int **));	// volumen
	
	for (i=0; i<L; i++)
	   {
	   		vol[i]= (int **) malloc(M*sizeof(int *));	// matriz
	   		
	   		for (j=0; j<M; j++)
	   		   {
	   		   	 vol[i][j]= (int *) malloc(N*sizeof(int)); // vector
	   		   	 
	   		   	 for (k=0; k<N; k++)
	   		   	    vol[i][j][k]= i*j*k;				// escalar
			   }
	   }
	   
	return(vol);
}

void imprimirVolumen(int ***vol, int L, int M, int N)
{
	int i=0, j=0, k=0;
	
	for (i=0; i<L; i++)
	   {
	   		printf("rebanada[%d]:\n", i);
	   		
	   		for (j=0; j<M; j++)
	   		   {
	   		   		for (k=0; k<N; k++)
	   		   		   printf("%d\t", vol[i][j][k]);
	   		   		   
	   		   		printf("\n");
			   }
			   
			printf("\n");
	   }
}


void destruirVolumenSegura(int ****vol, int L, int M)
{
	int ***q= NULL;
	
	q= *vol;
	
	destruirVolumenNoSegura(q, L, M);
	*vol= NULL;
}

void destruirVolumenNoSegura(int ***vol, int L, int M)
{
	int i=0, j=0;
	
	for (i=0; i<L; i++)
	   {
	   	 for (j=0; j<M; j++)
	   	    {
	   	    	free(vol[i][j]);	// vector
			}
			
		 free(vol[i]);				// matriz
	   }
	   
	free(vol);						// volumen
}


