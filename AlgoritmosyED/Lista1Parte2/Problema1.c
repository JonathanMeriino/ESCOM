//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
	int *arr= NULL;
	int N= 10;
	int k=0;
	
	printf("@ arr= %X\n", arr);

	arr= (int *) malloc(N*sizeof(int));
	
	printf("@ arr= %X\n", arr);

	for (k=0; k<N; k++)
	   printf("arr[%d]= %d\n", k, arr[k]);
	   
	printf("\n\n");

	for (k=0; k<N; k++)
	   arr[k]= 0;

	for (k=0; k<N; k++)
	   printf("arr[%d]= %d\n", k, arr[k]);
	   
	free(arr);	
	
	printf("@ arr= %X\n", arr);
	
	arr= NULL;
	
	printf("@ arr= %X\n", arr);	
	
	return 0;
}
