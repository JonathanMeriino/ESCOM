#include <stdio.h>
#include <stdlib.h>

#define VERDADERO 	1
#define FALSO		0

typedef struct elemento
{
	int dato;
}	t_elemento, *Elemento;

typedef struct nodo
{
	struct nodo *enlaceA;
	Elemento elem;
	struct nodo *enlaceB;
} t_nodo, *Nodo;


int main(int argc, char *argv[])
{
	return 0;
}

int crearElemento(Elemento *e)
{
	Elemento x= NULL;
	
	x= (Elemento) malloc(sizeof(t_elemento));
	
	if (x==NULL)
	  return(FALSO);
	  
	*e= x;  
	
	return(VERDADERO);
}

int destruirElemento(Elemento e)
{
	if (e==NULL)
	  return(FALSO);
	  
	free(e);
	return(VERDADERO);
}

int escribirDato(Elemento e, int dato)
{
	if (e==NULL)
	  return(FALSO);
	  
	e->dato= dato;
	
	return(VERDADERO);
}

int leerDato(Elemento e, int *dato)
{
	if (e==NULL)
	  return(FALSO);
	  
	*dato= e->dato;
	
	return(VERDADERO);
}


int crearNodo(Nodo *n)
{
	Nodo m= NULL;
	
	m= (Nodo) malloc(sizeof(t_nodo));
	
	if (m==NULL)
	  return(FALSO);
	
	m->enlaceA= NULL;
	m->elem= NULL;
	m->enlaceB= NULL;
	
	*n= m;
	
	return(VERDADERO);
}

int destruirNodo(Nodo n)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->elem= NULL;	//la destrucción del elemento se realiza por separado

	n->enlaceA= NULL;	
	n->enlaceB= NULL;
		
	free(n);
	
	return(VERDADERO);
}

int escribirElemento(Nodo n, Elemento e)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->elem= e;
	
	return(VERDADERO);
}

int leerElemento(Nodo n, Elemento *e)
{
	if (n==NULL)
	  return(FALSO);
	  
	*e= n->elem;
	
	return(VERDADERO);
}

int conectarEnlaceA(Nodo n, Nodo eA)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->enlaceA= eA;
	
	return(VERDADERO) ;
}

int conectarEnlaceB(Nodo n, Nodo eB)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->enlaceB= eB;
	
	return(VERDADERO) ;
}

int consultarEnlaceA(Nodo n, Nodo *eA)
{
	if (n==NULL)
	  return(FALSO);
	  
	*eA= n->enlaceA;
	
	return(VERDADERO) ;
}

int consultarEnlaceB(Nodo n, Nodo *eB)
{
	if (n==NULL)
	  return(FALSO);
	  
	*eB= n->enlaceB;
	
	return(VERDADERO) ;
}

int desconectarEnlaceA(Nodo n)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->enlaceA= NULL;
	
	return(VERDADERO) ;
}

int desconectarEnlaceB(Nodo n)
{
	if (n==NULL)
	  return(FALSO);
	  
	n->enlaceB= NULL;
	
	return(VERDADERO) ;
}



