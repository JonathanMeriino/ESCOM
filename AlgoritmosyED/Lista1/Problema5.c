//Codifique las funciones para ordenar y desordenar un arreglo de N enteros
#include <stdio.h>
#include <stdlib.h>

void ordenarArreglo(int *arreglo,int N)
{
int i,j,tam,aux;
  for(i=0;i<tam;i++)
      if(N[i]>N[j])
        aux=N[i];
        N[i]=N[j];
        N[j]=aux;
   printf("Los datos ordenados son: \n" );
   for(i=0;i<tam; i++)
      printf("%d\n",N[i] );
}
void desordenarArreglo(int *arreglo,int N)
{

}
int main(int argc, char const *argv[])
{
  int *arreglo, N[0];
  int tam,i;

  printf("Numeros a ingresar: \n");
  scanf("%d\n",&tam);

  for(i=0; i<tam; i++)
   printf("Ingresa el dato %d\n",i+1 );
   scanf("%d\n",&N [i]);

  ordenarArreglo(arreglo,N);
  desordenarArreglo(arreglo,N);

return 0;
}
