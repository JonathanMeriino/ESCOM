//Indique paso a paso que valores tienen las variables a,b,c,d,e y f y los apuntadores u,v,w,x,y,z.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

	int*u= NULL, *v= NULL, *w= NULL, *x= NULL, *y= NULL, *z= NULL; //Se define un puntero a Nulo
	int a=2, b=3, c=5, d=7, e=11, f=13;  //Se definen las variable de tipo entero

	u= &a;     //Se asigna la direccion de "a" a u
	*u= 90;     //Se asigna un valor a la direccion de memoria
	printf("Valor de a:%d\n", a);  //Imprime el valor de a

  v= &e; //Se asigna la direccion de e a v
	e++; //Incrementa su valor en 1
	printf("Valor de e: %d\n", e); //Se imprime el valor de e

  x= v; //Se asigna a x el valor de v
  printf("Valor de x: %d\n",*x ); //Accedemos al contenido de la direccion de memoria

  *u=(*u)-1;  //Se le asigna un valor a la direccion de memoria y se resta 1
	printf("Valor de a: %d\n", a); //Imprime el contenido de a

  *x= (*u) + 23; //Se le asigna valor a la direccion de memoria
	printf("Valor de *x: %d\n", *x); //Imprime el contenido de la direccion de memoria

  y= &c; //Se asigna la direccion de c a y
  printf("La direccion de memoria de c:%p \n",&c ); //Imprime la direccion de memoria c
  printf("Valor de y:%p\n", y); //Imprime la direccion de memoria de y
  w= &b;
  printf("La direccion de memoria de n es: %p \n",&b ); //Imprime la direccion de memoria de b
  printf("Valor de w:%p\n",w ); //Imprime la direccion de memoria de w

  d*= e; //Producto
	printf("Valor de d: %d\n", d); //Se imprime el resultado de f

  f--; //Se le resta 1 al valor de f
	printf("Valor de f: %d\n", f); //Imprime el valor de f

  z= &d; //Se le asigna la direccion de d a z
	(*z)+= 0;
  printf("Valor de z: %d\n", *z);

  u= v;
  printf("Valor de u: %d\n",*u); //Accedemos al contenido de direccion de memoria

  (*z)*= 6;
  printf("Valor de z: %d\n", *z);

	z = u;
  printf("Valor de z: %d\n",*z );

  *w= a+b+c+d+e+f;
  printf("Valor de w: %d\n", *w);

	*w-= 2019;
  printf("Valor de w: %d\n", *w);

	c++; //Se le suma 1 al valor de c
  printf("Valor: %d\n", c); //Se imprime el valor de c

	e--; //Se le resta 1 al valor de e
  printf("Valor: %d\n", e); //Se imprime el valor de e

	u= &a;
  printf("La direccion de memoria de a:%p \n",&a ); //Imprime la direccion de memoria c
  printf("Valor de u:%p\n", u); //Imprime valor de u
	v= &b;
  printf("La direccion de memoria de b:%p \n",&b ); //Imprime la direccion de memoria b
  printf("Valor de v:%p\n", v); //Imprime valor de v
	w= &c;
  printf("La direccion de memoria de c:%p \n",&c ); //Imprime la direccion de memoria c
  printf("Valor de w:%p\n", w); //Imprime valor de w

  *x= d + (*u);
  printf("Valor de x: %d\n", *x);

  *y= e+(*v);
  printf("Valor de y: %d\n", *y);

  *z= f + (*w);
  printf("Valor de z: %d\n", *z);

	return 0;
}
