#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[])
{
	int y= 0;
	int x= 23;
	int *p= NULL;
	int *q= NULL;
	
	p= &x;
	y= *p;
	
	y= (*p) + 50;
	
	y= 3*(*p);
	*p= 54;
	
	*p= (*p) + 10;
	(*p)+= 10;
	(*p)*= 10;
	
	printf("x= %d\n", x);
	
	printf("y= %d\n", y);
	
	// variable entera convencional:
	
	printf("el valor de x= %d\n", x);
	printf("la direccion de x= %X\n", &x);
	
	// apuntador:
	printf("el valor de p= %X\n", p);
	printf("la direccion de p= %X\n", &p);
	printf("el contenido a donde hace referencia p= %d\n", *p);
	
	p= &y;
	
	// variable entera convencional:
	
	printf("\n\n");
	
	printf("el valor de y= %d\n", y);
	printf("la direccion de y= %X\n", &y);
	
	// apuntador:
	printf("el valor de p= %X\n", p);
	printf("la direccion de p= %X\n", &p);
	printf("el contenido a donde hace referencia p= %d\n", *p);
	
	q= &y;
	
	printf("\n\n");
	
	// apuntador:
	printf("el valor de q= %X\n", q);
	printf("la direccion de q= %X\n", &q);
	printf("el contenido a donde hace referencia q= %d\n", *q);
	
	
	return 0;
}
