//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include <stdio.h>
#include <stdlib.h>

#define	VERDADERO 			1
#define FALSO				0
#define APUNTADORNULO		-1	

void imprimirCadena(char *cad);
void imprimirCadenaLongitud(char *cad, int N);
char *crearCadena(int N);
void destruirCadena(char *cad);
int copiarCadena(char *dest, char *fte);
int obtenerLongitudCadena(int *longitud, char *cad);
int buscarCadena(int *pos, char *cad, char *bsq);
int concatenarCadenas(char *fusion, char *cadA, char *cadB);

int main(int argc, char *argv[])
{
	char msg[100]= "Ejercicio 2";
	char *string= NULL;
	int num= 30, L=100, tamanho=0;
	int bandera= FALSO;
		
	printf("Cadena estatica:\n");
	imprimirCadena(msg);
	imprimirCadenaLongitud(msg, num);							
	
	printf("\nCadena dinamica: \n");
	string= crearCadena(L);
	bandera= copiarCadena(string, msg);
	
	if (bandera==VERDADERO)
	  imprimirCadena(string);
	else
	  printf("Error de copiado de cadena\n");
	  
	bandera= obtenerLongitudCadena(&tamanho, string);	//longitud= &tamanho;
	if (bandera==VERDADERO)
	  printf("longitud de la cadena= %d\n", tamanho);
	else
	  printf("Error al obtener la longitud de la cadena\n");

	destruirCadena(string);
	
	printf("\n");
	
	
	return 0;
}

void imprimirCadena(char *cad)
{
	int k=0;
	
	for (k=0; cad[k]!='\0'; k++)
	   printf("%c", cad[k]);
	
	printf("\n");  
	 
	//printf("%s\n", cad);
}

void imprimirCadenaLongitud(char *cad, int N)
{
	int k=0;
	
	for (k=0; k<N; k++)
	   printf("%c", cad[k]);
	
	printf("\n");  
	 
	//printf("%s\n", cad);
}

char *crearCadena(int N)
{
	char *cad= NULL;
	
	cad= (char *) malloc(N*sizeof(char));
	
	if (cad!=NULL)
	  cad[0]='\0';
	
	return(cad);
}

void destruirCadena(char *cad)
{
	free(cad);
	//cad= NULL;
}

int copiarCadena(char *dest, char *fte)
{
	int k=0;
	
	if (dest==NULL || fte==NULL)
	  return(FALSO);
	
	for (k=0; fte[k]!='\0'; k++)
	   dest[k]= fte[k];
	   
	dest[k]='\0';
	   
	return(VERDADERO);	   
}


int obtenerLongitudCadena(int *longitud, char *cad)
{
	int k=0;
	
	if (cad==NULL)
	  return(FALSO);
	  
	for (k=0; cad[k]!='\0'; k++);
	
	*longitud= k;
	
	return(VERDADERO);
}
