//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 

#include <stdio.h>
//Algoritmo por selección
int times=0; 

int main(void)
{
	// El arreglo
	int arreglo[] = {8,4,1,6,0,3,25,7,9};
	
	int longitud = sizeof(arreglo)/ sizeof(arreglo[0]);
	
	printf("Imprimiendo arreglo antes de ordenar...\n");
	int x = 0;
	for (x=0; x < longitud; x++)
	{
		printf("%d ", arreglo[x]);
  	}
  	
	printf("\n");
	
	seleccion(arreglo, longitud);
	
	//Imprimirlo después de ordenarlo
	printf("Imprimiendo arreglo despues de ordenar...\n");
	for (x = 0; x < longitud; x++)
		printf("%d ", arreglo[x]);
		
	printf("veces: %d", times); 
	
	return 0;
}

void seleccion(int arreglo[], int longitud)
{
	int i = 0;
	for (i = 0; i < longitud - 1; i++)
	{
		int j = i;
		for (j = i + 1; j < longitud; j++)
		{
			if (arreglo[i] > arreglo[j])
			{
				// ...intercambiarlos, es decir, mover el actual a la derecha y el de la derecha al actual
				intercambiar(&arreglo[i], &arreglo[j]);
				times++;
      		}
    	}
	}
}

void intercambiar(int *a, int *b)
{
	int temporal = *a;
	*a = *b;
	*b = temporal;
}
