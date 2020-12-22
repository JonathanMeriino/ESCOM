#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
	int **mat= NULL;
	int M= 10, N= 10;
	int i=0, j=0;
	
	// apartar memoria para el apuntador doble
	// conformado por M apuntadores sencillos:
	
	mat= (int **) malloc(M*sizeof(int *));
	
	
	// para cada apuntador sencillo, se reserva memoria
	// para sus N celdas (enteras)
	
	for (i=0; i<M; i++)
	   {
	   	 mat[i]= (int *) malloc(N*sizeof(int));
	   	 
	   	 for (j=0; j<N; j++)
	   	    mat[i][j]= i*j;
	   }
	   
	mat[3][2]= 42;
	
	for (i=0; i<M; i++)
	   {
	   	 for (j=0; j<N; j++)
	   	    printf("%d\t", mat[i][j]);
	   	 printf("\n");   
	   }
	   
	// liberar memoria de los apuntadores sencillos:
	
	for (i=0; i<M; i++)
	   free(mat[i]);
	   
	// libera memoria del apuntador doble:
	
	free(mat);
	
	return 0;
}
