//Indique paso a paso que valores tienen las variables a,b,c,d,e y f y los apuntadores u,v,w,x,y,z.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

	int*u= NULL, *v= NULL, *w= NULL, *x= NULL, *y= NULL, *z= NULL; //Se define un puntero a Nulo
	int a=2, b=3, c=5, d=7, e=11, f=13;  //Se definen las variable de tipo entero

	u= &a;     //Se asigna la direccion de "a" a u
	*u= 90;     //Se asigna un valor a la direccion de memoria
	printf("1. Valor de a:%d\n", a);  //Imprime el valor de a

  v= &e; //Se asigna la direccion de e a v
	e++; //Incrementa su valor en 1
	printf("2. Valor de e: %d\n", e); //Se imprime el valor de e

  x= v; //Se asigna a x el valor de v
  printf("3. Valor de x: %d\n",*x ); //Accedemos al contenido de la direccion de memoria

  *u=(*u)-1;  //Se le asigna un valor a la direccion de memoria y se resta 1
	printf("4. Valor de a: %d\n", a); //Imprime el contenido de a

  *x= (*u) + 23; //Se le asigna valor a la direccion de memoria
	printf("5. Valor de *x: %d\n", *x); //Imprime el contenido de la direccion de memoria

  y= &c; //Se asigna la direccion de c a y
  printf("6. La direccion de memoria de c:%p \n",&c ); //Imprime la direccion de memoria c
  printf("7. Valor de y:%p\n", y); //Imprime la direccion de memoria de y
  w= &b;
  printf("8. La direccion de memoria de n es: %p \n",&b ); //Imprime la direccion de memoria de b
  printf("9. Valor de w:%p\n",w ); //Imprime la direccion de memoria de w

  d*= e; //Producto
	printf("10. Valor de d: %d\n", d); //Se imprime el resultado de f

  f--; //Se le resta 1 al valor de f
	printf("11. Valor de f: %d\n", f); //Imprime el valor de f

  z= &d; //Se le asigna la direccion de d a z
	(*z)+= 0;
  printf("12. Valor de z: %d\n", *z);

  u= v;
  printf("13. Valor de u: %d\n",*u); //Accedemos al contenido de direccion de memoria

  (*z)*= 6;
  printf("14. Valor de z: %d\n", *z);

	z = u;
  printf("15. Valor de z: %d\n",*z );

  *w= a+b+c+d+e+f;
  printf("16. Valor de w: %d\n", *w);

	*w-= 2019;
  printf("17. Valor de w: %d\n", *w);

	c++; //Se le suma 1 al valor de c
  printf("18. Valor: %d\n", c); //Se imprime el valor de c

	e--; //Se le resta 1 al valor de e
  printf("19. Valor: %d\n", e); //Se imprime el valor de e

	u= &a;
  printf("20. La direccion de memoria de a:%p \n",&a ); //Imprime la direccion de memoria c
  printf("21. Valor de u:%p\n", u); //Imprime valor de u
	v= &b;
  printf("22. La direccion de memoria de b:%p \n",&b ); //Imprime la direccion de memoria b
  printf("23. Valor de v:%p\n", v); //Imprime valor de v
	w= &c;
  printf("24. La direccion de memoria de c:%p \n",&c ); //Imprime la direccion de memoria c
  printf("25. Valor de w:%p\n", w); //Imprime valor de w

  *x= d + (*u);
  printf("26. Valor de x: %d\n", *x);

  *y= e+(*v);
  printf("27. Valor de y: %d\n", *y);

  *z= f + (*w);
  printf("28. Valor de z: %d\n", *z);

	return 0;
}
