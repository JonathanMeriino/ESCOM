#include <stdio.h>
#include <stdlib.h>

#define VERDADERO	1
#define FALSO		0

int *crearArreglo(int N);
void imprimirArreglo(int *arr, int N);
void destruirArreglo(int *arr);
void destruirArregloCorrectamente(int **arr);

int crearArregloCorrectamente(int **arrEnvuelto, int M);
void destruirArregloCorrectamente(int **arrEnvuelto);

int main(int argc, char *argv[]) 
{
	int *tren= NULL;
	int N= 10;
	
	printf("\nInicio:\n");
	printf("direccion de tren= %X\n", &tren);
	printf("zona de memoria de tren= %X\n\n", tren);
	
	//tren= crearArreglo(N);
	crearArregloCorrectamente(&tren, N);		//arrEnvuelto= &tren;
												// tren= direccion de la zona de memoria dinamica
	printf("\nCreacion:\n");
	printf("direccion de tren= %X\n", &tren);
	printf("zona de memoria de tren= %X\n\n", tren);

	
	imprimirArreglo(tren, N);
	
	/*destruirArreglo(tren);
	printf("\nDestruccion:\n");
	printf("direccion de tren= %X\n", &tren);
	printf("zona de memoria de tren= %X\n\n", tren);*/
	
	destruirArregloCorrectamente(&tren);	// arrEnvuelto= &tren;
											// tren= NULL;
											
	printf("\nDestruccion con Apuntador Doble:\n");
	printf("direccion de tren= %X\n", &tren);
	printf("zona de memoria de tren= %X\n\n", tren);
	
	return 0;
}

int *crearArreglo(int M)
{
	int *arr= NULL;
	int k=0;
	
	arr= (int *) malloc(M*sizeof(int));
	
	for (k=0; k<M; k++)
	   arr[k]= 3*k;
	   
	return(arr);
}

void imprimirArreglo(int *arr, int M)
{
	int k=0;
	
	for (k=0; k<M; k++)
	   printf("[%d]= %d\n", k, arr[k]);
	   
	printf("\n");
}

void destruirArreglo(int *arr)
{
	printf("Funcion destruirArreglo: (antes de free)\n");
	printf("direccion de arr= %X\n", &arr);
	printf("zona de memoria de arr= %X\n\n", arr);
	
	free(arr);
	arr= NULL;
		
	printf("Funcion destruirArreglo: (despues de free)\n");
	printf("direccion de arr= %X\n", &arr);
	printf("zona de memoria de arr= %X\n\n", arr);
}

void destruirArregloCorrectamente(int **arrEnvuelto)	//arrEnvuelto= &tren;
{
	int *arr= NULL;
	
	arr= *arrEnvuelto;	// extrae arr;
	free(arr);
	*arrEnvuelto= NULL;
}

int crearArregloCorrectamente(int **arrEnvuelto, int M)
{
	int *arr= NULL;
	int k=0;
	
	arr= (int *) malloc(M*sizeof(int));
	
	if (arr==NULL)
	  return(FALSO);
	
	for (k=0; k<M; k++)
	   arr[k]= 3*k;
	   
	*arrEnvuelto= arr;
	   
	return(VERDADERO);
}

// los apuntadores dobles los podemos seguir
// trabajando como matrices dinamicas
// en las funciones

/*int **crearMatriz(int M, int N)
{
	int **mat= NULL;
	int i=0, j=0;
	
	mat= (int **) malloc(M*sizeof(int *));
	
	for (i=0; i<N; i++)
	   mat[i]= (int *) malloc(N*sizeof(int));
	   
	return(mat);
}

void imprimirMatriz(int **mat);
void destruirMatriz(int ***mat);*/







