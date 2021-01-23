/*En el siguiente codigo, determine los valores que van adquiriendo las variables y
los apuntadores tras la ejecucion de cada sentencia*/
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
  int *u= NULL, *v= NULL, *w= NULL, *q= NULL;
  int a= 101, b= 201, c= 301;
  u= &c; v= &b; w= &a;

  (*w)+= a + b + c;
  printf("1. Valor de w = %d\n", *w);
  (*u)++;
  printf("2. Valor de u = %d\n", *u);
  (*v)*= 4;
  printf("3. Valor de v = %d\n", *v);

  q= w; w= u; u= v; v= q;

  (*u)-= (*q)%5 - a;
  printf("4. Valor de u = %d\n", *u);
  (*v)-= (*q)%3 - b;
  printf("5. Valor de v = %d\n", *v);
  (*w)-= (*q)%2 - c;
  printf("6. Valor de w = %d\n", *w);

  printf("a=%d b=%d c= %d\n", a, b, c);
  return 0;
}
