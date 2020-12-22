#include <stdio.h>
#include <stdlib.h>

void funcion();
void enumerar(int N, int limite);
void arbolBinario(int nivel, int nodo, int limite);
void arbolTriple(int nivel, int nodo, int limite);
void arbolBase(int nivel, int nodo, int limite, int base, int *contador);

int main(int argc, char *argv[])
{
	int c=0, lim= 4, raiz=0, nivel=0, base=2;
	int conteo=0;
	
	// funcion();
	
	//enumerar(c, lim);
	//arbolBinario(nivel, raiz, lim);
	//arbolTriple(nivel, raiz, lim);
	arbolBase(nivel, raiz, lim, base, &conteo);
	
	printf("numero de nodos= %d\n", conteo);
		
	return 0;
}

void funcion()
{
	funcion();
}

void enumerar(int N, int limite)
{
	int k=0;
	
	if (N==limite)
	  return;
	
	for (k=0; k<N; k++)
	   printf("   ");	   
	printf("%d\n", N);
	
	enumerar(N+1, limite);
	enumerar(N+1, limite);
	
	for (k=0; k<N; k++)
	   printf("    ");	   
	printf("%d\n", N);
}

void arbolBinario(int nivel, int nodo, int limite)
{
	int k=0;
	
	if (nivel==limite)
	  return;
	
	for (k=0; k<nivel; k++)
	   printf("     ");	   
	printf("nodo= %d  nivel= %d\n", nodo, nivel);
	
	arbolBinario(nivel+1, 2*nodo + 0, limite);
	arbolBinario(nivel+1, 2*nodo + 1, limite);	
}

void arbolTriple(int nivel, int nodo, int limite)
{
	int k=0;
	
	if (nivel==limite)
	  return;
	
	for (k=0; k<nivel; k++)
	   printf("     ");	   
	printf("nodo= %d  nivel= %d\n", nodo, nivel);
	
	arbolTriple(nivel+1, 3*nodo + 0, limite);
	arbolTriple(nivel+1, 3*nodo + 1, limite);
	arbolTriple(nivel+1, 3*nodo + 2, limite);	
}

void arbolBase(int nivel, int nodo, int limite, int base, int *contador)
{
	int k=0;
	
	if (nivel==limite)
	  return;
	  
	(*contador)++;
	
	for (k=0; k<nivel; k++)
	   printf("     ");	   
	printf("nodo= %d  nivel= %d\n", nodo, nivel);
	
	for (k=0; k<base; k++)
	   arbolBase(nivel+1, base*nodo + k, limite, base, contador);
	   
}
