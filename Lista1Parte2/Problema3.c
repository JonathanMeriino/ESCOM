/*Despues de ejecutar cada sentencia, determine los valores que adquieren las
variables, los apuntadores sencillos y los apuntadores dobles*/
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
  int **q= NULL, *p= NULL;
  int *a= NULL, *b= NULL, *x= NULL, *y= NULL;
  int N= 10, k=0;
  a= (int *) malloc(N*sizeof(int));
  b= (int *) malloc(N*sizeof(int));
  for (x= a, y= b, k=0; k<N; k++, x++, y++)
      {
        (*x)= 2*k;
        (*y)= 3*k;
      }
  for (k=0; k<N; k++)
      {
        if (k%2==0)
          q= &a;
        else
          q= &b;
        p= *q;
        p= p+k;
        (*p)*= -1;

        (**q)+= *p;
      }
  for (k=0; k<N; k++)
      printf("%X :: a[%d] = %d\n", &(a[k]), k, a[k]);

  printf("\n");

  for (k=0; k<N; k++)
      printf("%X :: b[%d] = %d\n", &(b[k]), k, b[k]);
  free(a);
  free(b);
  return 0;
}
