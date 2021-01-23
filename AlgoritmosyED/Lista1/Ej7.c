//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include<stdio.h>
#include<math.h>

char *crearCadena(int N);
void imprimirCadena(int *arr, int N);
void destruirCadena(int crash, int test, int **arr, int dummy);

int main(int argc, char *argv[])
{
	char *q= NULL;
	int N= 100;
	
	printf("main inicio: &q= %X, q= %X\n", &q, q);
	
	q= crearCadena(N);
	
	printf("main creacion: &q= %X, q= %X\n\n", &q, q);
	
	imprimirCadena(q, N);
	
	destruirCadena(1952, 1812, &q, 2020);
	printf("main destruccion: &q= %X, q= %X\n\n", &q, q);
	imprimirCadena(q, N);
	
	
	return 0;
}

char *crearCadena(int N)
{
	int *arr= NULL;
	int k=0;
	
	arr= (int *) malloc(N*sizeof(int));
	
	if (arr==NULL)
	  return(NULL);
	  
	for (k=0; k<N; k++)
	   arr[k]= 2*k;
	   
	return(arr);
}

void imprimirCadena(int *arr, int N)
{
	int k=0;
	
	printf("imprimir: &arr= %X, arr= %X\n\n", &arr, arr);
		
	if (arr==NULL)
	  return;
	  
	  
	for (k=0; k<N; k++)
       printf("%d ", arr[k]);
	   
	printf("\n\n");		
}

void destruirCadena(int crash, int test, int **arr, int dummy)
{
	int *cadena= NULL;
	
	cadena= *arr;
	
	printf("segura: &arr= %X, arr= %X, *arr= %X\n\n", &arr, arr, *arr);
	free(cadena);
	*arr= NULL;
}


