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
	char msg[100]= "peter parker";	// implicitamente se agrega
									// el caracter de fin de cadena
									// '\0'
	char *string= NULL;
	int num= 30, L=100, tamanho=0;
	int bandera= FALSO;
	
	char enunciado[100]= "desayunardesayuno@@@@@";
	char palabra[100]= "desayuno";
	int localidad=-1;
	char *fusion=NULL;
			
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
	
	printf("Introduzca enunciado: ");
	gets(enunciado);
	//scanf("%s", enunciado);
	
	printf("Introduzca palabra: ");
	gets(palabra);
	//scanf("%s", palabra);
	
	printf("enunciado= %s\n", enunciado);
	printf("palabra= %s\n", palabra);
	buscarCadena(&localidad, enunciado, palabra);
	printf("localidad= %d\n", localidad);
	
	printf("\n\n");
	
	fusion= crearCadena(200);
	concatenarCadenas(fusion, enunciado, palabra);
	printf("concatenacion: %s\n", fusion);
	destruirCadena(fusion);
	
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

// UML: Unified Modeling Language
// cad: arreglo de caracteres de memoria dinamica
// longitud: apuntador de referencia a una variable entera

int obtenerLongitudCadena(int *longitud, char *cad)
{
	int k=0;
	
	if (cad==NULL)
	  return(FALSO);
	  
	for (k=0; cad[k]!='\0'; k++);
	
	*longitud= k;
	
	return(VERDADERO);
}

int buscarCadena(int *pos, char *cad, char *bsq)
{
	int i=0, j=0;
	
	*pos= -1;
	
	if (cad==NULL || bsq==NULL)
	  return(FALSO);
	
	for (i=0; cad[i]!='\0'; i++)
	   {
	   		for (j=0; cad[i+j]==bsq[j] && cad[i+j]!='\0' && bsq[j]!='\0'; j++);
	   		
	   		if (bsq[j]=='\0')
	   		  {				 
	   		  	*pos= i;
	   		  	return(VERDADERO);
	   		  }
	   }
	
	return(FALSO);
}


int concatenarCadenas(char *fusion, char *cadA, char *cadB)
{
	int i=0, j=0;
	
	if (fusion==NULL || cadA==NULL || cadB==NULL)
	  return(FALSO);
	  
	for (i=0; cadA[i]!='\0'; i++)
	   fusion[i]= cadA[i];
	   
	for (j=0; cadB[j]!='\0'; j++, i++)
	   fusion[i]= cadB[j];
	
	fusion[i]= '\0';
	
	return(VERDADERO);
}




















