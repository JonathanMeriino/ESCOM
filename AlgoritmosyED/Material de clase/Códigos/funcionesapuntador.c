#include <stdio.h>
#include <stdlib.h>

void imprimirCaracter(char c);
void cambiarCaracter(char *w);
char dispararCaracter(char v);

int main(int argc, char *argv[]) 
{
	char letra= 'A', garabato= ' ';
	//char *p= NULL;
	
	char *q= NULL;
	char *cadena= NULL;

	imprimirCaracter(letra);	// c= letra;	// se copia el valor
	printf("letra= %c\n", letra);
	
	//p= &letra;
	//cambiarCaracter(p);
	
	cambiarCaracter(&letra);	// w= &letra;	// se copia una direccion
	printf("letra= %c\n", letra);
	
	letra='A';
	garabato= dispararCaracter(letra);
	printf("letra= %c garabato= %c \n", letra, garabato);
	
	return 0;
}

void imprimirCaracter(char c)	// paso por copia o valor
{
	printf("caracter por copia de valor= %c\n", c);
	c= 'B';
}

void cambiarCaracter(char *w)	// paso por referencia
{
	char h= ' ';
	
	h= *w;		//consulta
	
	printf("caracter via apuntador= %c\n", h);
	
	*w= 'B';	// modificacion
}

char dispararCaracter(char v)	// solamente hace transferencia de valores
{
	printf("caracter en el revolver= %c\n", v);	// lee copia del valor
	v= 'B';
	return(v);					// regresa la copia del valor
}

