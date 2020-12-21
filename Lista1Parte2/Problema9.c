/*Calcule la complejidad computacional de cada uno de los ciclos que forman parte
del siguiente codigo. ¿Cual es el valor de la variable x que se despliega en consola
entre iteraciones*/
#include<stdio.h>
#include<stdlib.h>
int main(int argc, char *argv[])
{
  int k=0, x=0, i=0, j=0;
  for (k=0, x=0; k<N; k++)
      x+= k;

  printf("x= %d\n");

  for (k=1, x=0; k<N; k*=6)
      x+= k;

  printf("x= %d\n");

  for (i=0, x=0; i<N; i+=2)
      for (j=0; j<N; j+=3)
            x+= i*j;

  printf("x= %d\n");

  for (i=N, x=0; i>0; i/=2)
      for (j=N; j>0; j--)
          x+= i*j;

  printf("x= %d\n");
}
