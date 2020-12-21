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
  (*u)++;
  (*v)*= 4;

  q= w; w= u; u= v; v= q;

  (*u)-= (*q)%5 - a;
  (*v)-= (*q)%3 - b;
  (*w)-= (*q)%2 - c;
  printf("a=%d b=%d c= %d\n", a, b, c);
  return 0;
}
