#include <stdio.h>
#include <stdlib.h>

int *crearArreglo(int N);
//void destruirArregloFormaNoSegura(int *arr);
void imprimirArreglo(int *arr, int N);
void destruirArregloFormaNoSegura(int crash, int test, int *arr, int dummy);
void destruirArregloFormaSegura(int crash, int test, int **arr, int dummy);

int main(int argc, char *argv[])
{
	int *q= NULL;
	int N= 100;
	
	printf("main inicio: &q= %X, q= %X\n", &q, q);
	
	q= crearArreglo(N);
	
	printf("main creacion: &q= %X, q= %X\n\n", &q, q);
	
	imprimirArreglo(q, N);
	
	//destruirArregloFormaNoSegura(1952, 1812, q, 2020);
	
	destruirArregloFormaSegura(1952, 1812, &q, 2020);
	
	printf("main destruccion: &q= %X, q= %X\n\n", &q, q);
	
	imprimirArreglo(q, N);
	
	
	return 0;
}

int *crearArreglo(int N)
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

void destruirArregloFormaNoSegura(int crash, int test, int *arr, int dummy)
{
	printf("destruir: &arr= %X, arr= %X\n\n", &arr, arr);
	
	free(arr);
	arr= NULL;
}

/*void destruirArregloFormaSegura()
{
	
}*/

void imprimirArreglo(int *arr, int N)
{
	int k=0;
	
	printf("imprimir: &arr= %X, arr= %X\n\n", &arr, arr);
		
	if (arr==NULL)
	  return;
	  
	  
	for (k=0; k<N; k++)
       printf("%d ", arr[k]);
	   
	printf("\n\n");		
}


void destruirArregloFormaSegura(int crash, int test, int **arr, int dummy)
{
	int *tren= NULL;
	
	tren= *arr;
	
	printf("segura: &arr= %X, arr= %X, *arr= %X\n\n", &arr, arr, *arr);
	free(tren);
	*arr= NULL;
}

