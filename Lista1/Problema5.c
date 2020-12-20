#include <stdio.h>
#include <stdlib.h>

void leerArreglo(int *arreglo,int N)
{
 int tam,i;

 printf("Numeros a ingresar: \n");
 scanf("%d\n",&tam);

 for(i=0; i<tam; i++)
  printf("Ingresa el dato %d\n",i+1 );
  scanf("%d\n",&N [i]);
}
void ordenarArreglo(int *arreglo,int N[])
{
int i,j,tam,aux;
  for(i=0;i<tam;i++)
      if(N[i]>N[j])
        aux=N[i];
        N[i]=N[j];
        N[j]=aux;
   printf("Los datos ordendsos son: \n" );
   for(i=0;i<tam; i++)
      printf("%d\n",N[i] );
}
void desordenarArreglo(int *arreglo,int N)
{

}
int main(int argc, char const *argv[])
{
  int *arreglo, N;
  leerArreglo(arreglo,N[]);
  ordenarArreglo(arreglo,N[]);
  desordenarArreglo(arreglo,N[]);

return 0;
}
