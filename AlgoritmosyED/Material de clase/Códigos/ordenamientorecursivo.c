#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NOLOCALIZADO	-1

int buscarBinariamente(int *arr, int num, int inf, int sup, int N);
void ordenarRapidamente(int *arr, int inf, int sup);
void imprimirArreglo(int *arr, int N);
void desordenarArreglo(int *arr, int N);
void ordenarPorRecombinacion(int *arr, int inf, int sup);
void recombinar(int *arr, int inf, int mitad, int sup);

int main(int argc, char *argv[])
{
	int arr[10]= {5, 11, 12, 15, 20, 31, 35, 42, 54, 98};
	int N= 10;
	int num= 35, inf=0, sup=N-1;
	int pos= NOLOCALIZADO;
	
	pos= buscarBinariamente(arr, num, inf, sup, N);
	printf("el numero %d se encuentra en la posicion %d\n", num, pos);
	
	desordenarArreglo(arr, N);
	imprimirArreglo(arr, N);
	//ordenarRapidamente(arr, inf, sup);
	ordenarPorRecombinacion(arr, inf, sup);
	imprimirArreglo(arr, N);
	
	return 0;
}

int buscarBinariamente(int *arr, int num, int inf, int sup, int N)
{
	int mitad= 0, localidad= NOLOCALIZADO;
	int k=0;
	
	if (inf>sup)
	  return(NOLOCALIZADO);
	
	mitad= inf + (sup-inf)/2;
		// mitad= (sup-inf)/2;
	    // mitad= inf + mitad;

	if (num==arr[mitad])
	  return(mitad);
	  
	if (num>arr[mitad])
	  localidad= buscarBinariamente(arr, num, mitad+1, sup, N);
	else
	  localidad= buscarBinariamente(arr, num, inf, mitad-1, N);
	
	return(localidad);
}

void ordenarRapidamente(int *arr, int inf, int sup)
{
	int pivote= 0, aux= 0;
	
	if (inf>sup)
	  return;
	  	
	pivote= permutarArreglo(arr, inf, sup);
	
	ordenarRapidamente(arr, inf, pivote-1);
	ordenarRapidamente(arr, pivote+1, sup);
}

int permutarArreglo(int *arr, int inf, int sup)
{
	int k=inf, pivote=sup;
	int aux=0;
	
	while(k<pivote)
	   {
	   	 if (arr[k]>arr[pivote])			// comparacion de referencias
	   	   {	
	   	     // permutacion:
	   	     
			  if (k+1<pivote)
			    {								
	   	   	  		aux= arr[pivote-1];		
	   	   	  		arr[pivote-1]= arr[pivote];
	   	   	  	}
	   	   	  else
				aux= arr[pivote];
				
	   	   	  arr[pivote]= arr[k];
	   	   	  arr[k]= aux; 	   	  
	   	   	  pivote--;
		   }
		 else
		   k++;
	   }
	
	return(pivote);
}

void desordenarArreglo(int *arr, int N)
{
	int k=0, q=0, aux=0;
	
	srand(time(NULL));
	
	for (k=0; k<N; k++)
	   {
	   	 q= rand()%N;
	   	 aux= arr[q];
		 arr[q]= arr[k];
		 arr[k]= aux; 
	   }	
}

void imprimirArreglo(int *arr, int N)
{
	int k=0;
	
	for (k=0; k<N; k++)
	   printf("%d ", arr[k]);
	   
	printf("\n");
}

void ordenarPorRecombinacion(int *arr, int inf, int sup)
{
	int mitad=0;
	
	if (inf>=sup)
	  return;
	  
	mitad= inf+(sup-inf)/2;
	
	ordenarPorRecombinacion(arr, inf, mitad);
	ordenarPorRecombinacion(arr, mitad+1, sup);
	
	recombinar(arr, inf, mitad, sup);
}

void recombinar(int *arr, int inf, int mitad, int sup)
{
	int i=0, j=0, k=0, q=0;
	int *aux= NULL;
	int L= sup - inf + 1;
	
	aux= (int *) malloc(L*sizeof(int));
	
	for (k=0, i=inf, j=mitad+1; k<L; k++)
	   {
	   	 if (arr[i] < arr[j] && i<=mitad || j>sup)
	   	   {
	   	   	 	aux[k]= arr[i];
	   	   	 	i++;
		   }
		 else
		   {
		   	 if (arr[i] >= arr[j] && j<=sup || i>mitad)
		   	   {				  
		   	   		aux[k]= arr[j];
		   	   		j++;
		   	   }
		   }
	   }
	   
	for (k=0, q= inf; k<L; k++, q++)
	   arr[q]= aux[k];
	   
	free(aux);
}

//quicksort
//mergesort
//heapsort

