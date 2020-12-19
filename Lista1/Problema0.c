#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

	int*u= NULL, *v= NULL, *w= NULL, *x= NULL, *y= NULL, *z= NULL;
	int a=2, b=3, c=5, d=7, e=11, f=13;

	u= &a;
	*u= 90;
	printf("Valor:%d\n", a);

  v= &e;
	e++;
	printf("Valor: %d\n", e);

  x= v;
	*u=(*u)-1;
	printf("Valor: %d\n", a);

  *x= (*u) + 23;
	printf("Valor: %d\n", e);

  y= &c;
	w= &b;
	d*= e;
	printf("Valor: %d\n", d);

  f--;
	printf("Valor: %d\n", f);

  z= &d;
	(*z)+= 0;
  printf("Valor: %d\n", d);

  u= v;
	(*z)*= 6;
  printf("Valor: %d\n", d);

	z = u;
	*w= a+b+c+d+e+f;
  printf("Valor: %d\n", b);

	*w-= 2019;
  printf("Valor%d\n", b);

	c++;
  printf("Valor: %d\n", c);

	e--;
  printf("Valor: %d\n", e);

	u= &a;
	v= &b;
	w= &c;
	*x= d + (*u);
  printf("Valor: %d\n", e);

  *y= e + (*v);
  printf("Valor: %d\n", c);

  *z= f + (*w);
  printf("Valor: %d\n", e);

	return 0;
}
