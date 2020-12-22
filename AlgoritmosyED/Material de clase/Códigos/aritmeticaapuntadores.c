#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
	int x= 38;
	int *p= NULL;
	int *arr= NULL;
	int N= 10, k=0;
	int *q= NULL;
	
	p= &x;
	
	printf("valor de x= %d\n", x);
	printf("direccion de x= %X\n\n", &x);
	
	printf("valor de p= %X\n", p);
	printf("direccion de p= %X\n", &p);
	printf("contenido a donde hace referencia p= %d\n\n", *p);
	
	printf("valor de arr= %X\n", arr);
	printf("la direccion de arr= %X\n\n", &arr);
	
	arr= (int *) malloc(N*sizeof(int));
	
	printf("valor de arr (malloc)= %X\n", arr);
	
	for (k=0; k<N; k++)
	   arr[k]= 6*k;
	   
	for (k=0; k<N; k++)
	   printf("[%d]= %d\t::\t#%X\n", k, arr[k], &(arr[k]));
	   
	// la direccion de la celda k: &(arr[k])
	
	printf("\n");
	
	q= arr;
	printf("la direccion de q= %X\n", &q);
	printf("valor de q= %X\n", q);
	   	
	for (k=0; k<N; k++)
	   {
	   	  printf("k= %d \t q= %X \t *q= %d\n", k, q, *q);
	   	  q++;
	   }
	   
	printf("\n");
	printf("Modificacion del arreglo via q:\n");
	
	/*q= arr;
	   
	for (k=0; k<N; k++)
	   {
	   	  *q= 9*k;
	   	  q++;
	   }*/
	   
	for (k=0, q= arr; k<N; k++, q++)
	   *q= 9*k;
	
	q= arr;
	/*q++;
	q++;
	q++;
	q++;
	q++;*/
	
	q= q + 5;		/// direccion donde apunta q, avanza 5*4= 20 bytes
					// 5: 5 enteros después, 4: tamaño de cada entero 
	*q= 1253;
	
	
	q= arr;
	
	for (k=0; k<N; k++)
	   {
	   	  printf("k= %d \t q= %X \t *q= %d\n", k, q, *q);
	   	  q++;
	   }
	
	printf("\nEstado final del arreglo dinamico:\n");
	
	for (k=0; k<N; k++)
	   printf("[%d]= %d\t::\t#%X\n", k, arr[k], &(arr[k]));
	   
	free(arr);
	
	return 0;
}
