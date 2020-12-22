#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define VERDADERO		1
#define FALSO			0
#define CARTESIANO		1
#define POLAR			0

// TAD: tipo abstracto de datos numero complejo:

typedef struct complejo
{
	float real;
	float imaginario;
	float magnitud;
	float argumento;	
}t_complejo, *Complejo;

// Complejo = (struct complejo *)

// int *arr= (int *) malloc(N*sizeof(int));

// struct complejo *c= (struct complejo *) malloc(1*sizeof(struct complejo));

// Complejo c= (Complejo) malloc(sizeof(t_complejo));

// i= sqrt(-1);
// z= real + i imaginario;			z= x+iy;
// z= magnitud*exp(i*argumento);	z= r*exp(i*arg);

Complejo crearNumeroComplejo(float a, float b, int formato);
int crearNumeroComplejoReferencia(Complejo *z, float a, float b, int formato);
void imprimirNumeroComplejo(Complejo z, int formato);
int destruirNumeroComplejo(Complejo *z);
int sumarNumerosComplejos(Complejo *z, Complejo z0, Complejo z1);
int multiplicarNumerosComplejos(Complejo *z, Complejo z0, Complejo z1);
int obtenerComponenteReal(Complejo z, float *x);
int obtenerComponenteImaginaria(Complejo z, float *y);
int obtenerMagnitud(Complejo z, float *r);
int obtenerArgumento(Complejo z, float *a);

int main(int argc, char *argv[]) 
{
	Complejo zA= NULL;
	Complejo zB= NULL;
	Complejo zC= NULL;
	
	zA= crearNumeroComplejo(1.0, 0.0, CARTESIANO);
	crearNumeroComplejoReferencia(&zB, 1.0, M_PI/2.0, POLAR);	
	crearNumeroComplejoReferencia(&zC, 0.0, 0.0, CARTESIANO);
	
	printf("zA= ");
	imprimirNumeroComplejo(zA, CARTESIANO);
	printf("zA= ");
	imprimirNumeroComplejo(zA, POLAR);	
	
	printf("zB= ");
	imprimirNumeroComplejo(zB, CARTESIANO);
	printf("zB= ");
	imprimirNumeroComplejo(zB, POLAR);

	sumarNumerosComplejos(&zC, zA, zB);
	printf("zC= zA + zB = ");
	imprimirNumeroComplejo(zC, CARTESIANO);
	printf("zC= zA + zB = ");
	imprimirNumeroComplejo(zC, POLAR);	
	
	multiplicarNumerosComplejos(&zC, zA, zB);
	printf ("zC= zA * zB = ");
	imprimirNumeroComplejo(zC, CARTESIANO);
	printf ("zC= zA * zB = ");
	imprimirNumeroComplejo(zC, POLAR);

	destruirNumeroComplejo(&zC);
	destruirNumeroComplejo(&zB);
	destruirNumeroComplejo(&zA);
	
	return 0;
}

Complejo crearNumeroComplejo(float a, float b, int formato)
{
	Complejo z= NULL;
	
	z= (Complejo) malloc(sizeof(t_complejo));
	
	if (z==NULL)
	  return(NULL);
	  
	if (formato==CARTESIANO)
	  {
		z->real= a;				// x= a
		z->imaginario= b;		// y= b
	
		z->magnitud= sqrt(a*a+b*b);		// r= sqrt(x^2+y^2)
		z->argumento= atan2(b,a);		// arg= atan(y/x)
	  }
	else
	  {
	  	z->magnitud= a;			// r= a 
	  	z->argumento= b;		// arg= b
	  	
	  	z->real= a*cos(b);			// x= r*cos(arg);
	  	z->imaginario= a*sin(b);	// y= r*sin(arg);
	  }
	  
	return(z);	
}
									
int crearNumeroComplejoReferencia(Complejo *z, float a, float b, int formato)
{
	Complejo c= NULL;
	
	c= crearNumeroComplejo(a, b, formato);
	
	if (c==NULL)
	  {
	  	*z= NULL;
	  	return(FALSO);
	  }
	
	*z= c;
	
	return(VERDADERO);
}

void imprimirNumeroComplejo(Complejo z, int formato)
{
	if (z==NULL)
	  return;
	
	if (formato==CARTESIANO)  
	  printf("%0.4f + i %0.4f\n", z->real, z->imaginario);
	else
	  printf("%0.4f e^(i %0.4f PI)\n", z->magnitud, z->argumento/M_PI);	
}

int destruirNumeroComplejo(Complejo *z)
{
	if (*z==NULL)
	  return(FALSO);

	// liberar antes contenido de la estructura si es necesario
		  
	free(*z);
	*z= NULL;
	
	return(VERDADERO);
}

int sumarNumerosComplejos(Complejo *z, Complejo z0, Complejo z1)
{
	float x=0.0, y=0.0;
	
	if (*z==NULL || z0==NULL || z1==NULL)
	  return(FALSO);
	  
	(*z)->real= z0->real + z1->real;
	(*z)->imaginario= z0->imaginario + z1->imaginario;

	x= (*z)->real;
	y= (*z)->imaginario;
	
	(*z)->magnitud= sqrt(x*x+y*y);
	(*z)->argumento= atan2(y, x);
	
	return(VERDADERO);
}

int multiplicarNumerosComplejos(Complejo *z, Complejo z0, Complejo z1)
{
	float r=0.0, a=0.0;
	
	if (*z==NULL || z0==NULL || z1==NULL)
	  return(FALSO);
	  
	(*z)->magnitud= (z0->magnitud) * (z1->magnitud);
	(*z)->argumento= (z0->argumento) + (z1->argumento);

	r= (*z)->magnitud;
	a= (*z)->argumento;
	
	(*z)->real= r*cos(a);
	(*z)->imaginario= r*sin(a);
	
	return(VERDADERO);
}

int obtenerComponenteReal(Complejo z, float *x)
{
	if (z==NULL)
	  return(FALSO);
	  
	*x= z->real;
	return(VERDADERO);
}

int obtenerComponenteImaginaria(Complejo z, float *y)
{
	if (z==NULL)
	  return(FALSO);
	  
	*y= z->imaginario;
	return(VERDADERO);
}

int obtenerMagnitud(Complejo z, float *r)
{
	if (z==NULL)
	  return(FALSO);
	  
	*r= z->magnitud;
	return(VERDADERO);
}

int obtenerArgumento(Complejo z, float *a)
{
	if (z==NULL)
	  return(FALSO);
	  
	*a= z->argumento;
	return(VERDADERO);
}

