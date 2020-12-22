#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
	int *arr= NULL;
	//char *nombre= NULL;
	int N= 10;
	int k=0;
	
	printf("@ arr= %X\n", arr);
	
	// asignacion de memoria:
	arr= (int *) malloc(N*sizeof(int));
	//nombre= (char *) malloc(N*sizeof(char));
	
	printf("@ arr= %X\n", arr);
	
	// estado del arreglo dinamico reservado:
	for (k=0; k<N; k++)
	   printf("arr[%d]= %d\n", k, arr[k]);
	   
	printf("\n\n");
	   
	// inicializacion del arreglo dinamico:
	for (k=0; k<N; k++)
	   arr[k]= 0;
	   
	// estado del arreglo dinamico al ser inicializado:
	for (k=0; k<N; k++)
	   printf("arr[%d]= %d\n", k, arr[k]);
	   
	// liberacion de memoria:
	free(arr);	
	
	printf("@ arr= %X\n", arr);
	
	arr= NULL;
	
	printf("@ arr= %X\n", arr);	
	
	return 0;
}
