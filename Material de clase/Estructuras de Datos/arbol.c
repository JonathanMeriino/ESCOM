#include <stdio.h>
#include <stdlib.h>

#include <stdio.h>
#include <stdlib.h>


#define VERDADERO 1
#define FALSO     0

typedef struct nodo
{
  int dato;
  struct nodo *enlaceDer;
  struct nodo *enlaceIzq;
} tnodo, *Nodo;

typedef struct arbol
{
  Nodo raiz;
  int cantidad;
} tarbol, *Arbol;

Nodo crearNodo(void);
int escribirDato(Nodo n, int dato);
int leerDato(Nodo n, int *dato);
void destruirNodo(Nodo n);

int conectarNodoDerecho(Nodo n, Nodo conexion);
int conectarNodoIzquierdo(Nodo n, Nodo conexion);
int desconectarNodo(Nodo n);
Nodo consultarEnlaceIzquierdo(Nodo n);
Nodo consultarEnlaceDerecho(Nodo n);

Arbol crearArbol(void);
void destruirArbol(Arbol a);
void destruirNodosRecursivamente(Nodo central);
int insertarDato(Arbol a, int dato);
Nodo insertarDatoRecursivo(Nodo central, int dato);
int buscarDato(Arbol a, int dato);
Nodo buscarDatoRecursivo(Nodo central, int dato);
Nodo buscarMinimo(Nodo central);
Nodo buscarMaximo(Nodo central);
int eliminarDato(Arbol a, int dato);
int eliminarDatoRecursivo(Nodo central, int dato);

int recorrerArbolEnOrden(Arbol a);
void recorrerNodosEnOrden(Nodo central);
int recorrerArbolPreOrden(Arbol a);
void recorrerNodosPreOrden(Nodo central);
int recorrerArbolPostOrden(Arbol a);
void recorrerNodosPostOrden(Nodo central);

int recorrerArbolEnOrdenDescendente(Arbol a);
void recorrerNodosEnOrdenDescendente(Nodo central);


int main(int argc, char *argv[])
{
	Arbol arbol= NULL;
	
	arbol= crearArbol();
	
	if (arbol!=NULL)
	  {
		insertarDato(arbol, 72);
		insertarDato(arbol, 7);
		insertarDato(arbol, 13);
		insertarDato(arbol, 9);
		insertarDato(arbol, 23);
		insertarDato(arbol, 12);
		insertarDato(arbol, 78);
		insertarDato(arbol, 55);

		insertarDato(arbol, 17);
		insertarDato(arbol, 41);
		insertarDato(arbol, 36);
		insertarDato(arbol, 99);
		insertarDato(arbol, 32);
		insertarDato(arbol, 31);
		insertarDato(arbol, 63);
		insertarDato(arbol, 28);

		insertarDato(arbol, 10);
		insertarDato(arbol, 30);
		insertarDato(arbol, 67);
		insertarDato(arbol, 2);
		insertarDato(arbol, 8);
		insertarDato(arbol, 5);
		insertarDato(arbol, 88);
		insertarDato(arbol, 43);
	
		recorrerArbolEnOrden(arbol);
		
		eliminarDato(arbol, 31);
		
		recorrerArbolEnOrden(arbol);
		
		// recorrerArbolPreOrden(arbol);
		
		// recorrerArbolPostOrden(arbol);
		
		// recorrerArbolEnOrdenDescendente(arbol);
		
		destruirArbol(arbol);
	  }
	return 0;
}

Nodo crearNodo(void)
{
	Nodo n= NULL;
	
	n= (Nodo) malloc(sizeof(tnodo));
	
	n->enlaceIzq= NULL;
	n->enlaceDer= NULL;
	n->dato= 0;
	
	return(n);
}

int escribirDato(Nodo n, int dato)
{
  if (n==NULL)
    return(FALSO);
    
  n->dato= dato;
  return(VERDADERO);    
}

int leerDato(Nodo n, int *dato)
{
  if (n==NULL)
    return(FALSO);
    
  *dato= n->dato;
  
  return(VERDADERO);    
}

void destruirNodo(Nodo n)
{
	if (n!=NULL)
	  {
	  	n->enlaceIzq= NULL;
	  	n->enlaceDer= NULL;
	  	free(n);
	  	n= NULL;
	  }
}

int conectarNodoDerecho(Nodo n, Nodo conexion)
{
	if (n==NULL || conexion==NULL)
	  return(FALSO);
	
	n->enlaceDer= conexion;
  
	return(VERDADERO);  
}

int conectarNodoIzquierdo(Nodo n, Nodo conexion)
{
	if (n==NULL || conexion==NULL)
	  return(FALSO);
	
	n->enlaceIzq= conexion;
	  
	return(VERDADERO);  
}

int desconectarNodo(Nodo n)
{
	if (n==NULL)
	  return(FALSO);
	
	n->enlaceIzq= NULL;
	n->enlaceDer= NULL;
	  
	return(VERDADERO);  
}

Nodo consultarEnlaceIzquierdo(Nodo n)
{
	if (n!=NULL)
	  return(n->enlaceIzq);
	  
	return(NULL);  
}

Nodo consultarEnlaceDerecho(Nodo n)
{
	if (n!=NULL)
	  return(n->enlaceDer);
	  
	return(NULL);  
}/*************************************/

Arbol crearArbol(void)
{
	Arbol a= NULL;
	
	a= (Arbol) malloc(sizeof(tarbol));
	
	if (a!=NULL)
	  {
	  	a->cantidad=0;
	  	a->raiz= NULL;
	  }
	
	return(a);
}

void destruirArbol(Arbol a)
{
	if (a==NULL)
	  return;
	  
	if (a->raiz!=NULL)
	  destruirNodosRecursivamente(a->raiz);
	  
	if (a->raiz!=NULL)
	  destruirNodo(a->raiz);
	  
	a->raiz= NULL;
	a->cantidad= 0;
	
	free(a);    
}

void destruirNodosRecursivamente(Nodo central)
{
	Nodo izq=NULL, der=NULL;
	
	if (central==NULL)
	  return;
	  
	izq= central->enlaceIzq;
	der= central->enlaceDer;
	
	if (izq!=NULL)
	  {	  
	    central->enlaceIzq= NULL;
	    destruirNodosRecursivamente(izq);   
	  }
	  
	if (der!=NULL)
	  {	  
	    central->enlaceDer= NULL;
	    destruirNodosRecursivamente(der);   
	  }
	  
	if (izq==NULL && der==NULL)
	  destruirNodo(central);
}

int insertarDato(Arbol a, int dato)
{
	Nodo nuevo= NULL;
	
	if (a==NULL)
	  return(FALSO);
	  
	nuevo= insertarDatoRecursivo(a->raiz, dato);  
	
	if (a->raiz==NULL)
	  a->raiz= nuevo;
	  
	if (nuevo!=NULL)
	  a->cantidad++;  
	
	return(VERDADERO);  
}

Nodo insertarDatoRecursivo(Nodo central, int dato)
{
	Nodo nuevo= NULL;
	Nodo izq= NULL, der= NULL;
	
	if (central==NULL)
	  {
	  	nuevo= crearNodo();
	  	if (nuevo!=NULL)
	  	  nuevo->dato= dato;
	  	return(nuevo);  
	  }
	  
	izq= central->enlaceIzq;
	der= central->enlaceDer;
	
	if (dato<central->dato)
	  {
	  	nuevo= insertarDatoRecursivo(izq, dato);
	  	if (izq==NULL)
	  	  central->enlaceIzq= nuevo;
	  }
	  
	if (dato>central->dato)
	  {
	  	nuevo= insertarDatoRecursivo(der, dato);
	  	if (der==NULL)
	  	  central->enlaceDer= nuevo;
	  }	 
	  
   return(nuevo);	   
}

int buscarDato(Arbol a, int dato)
{
	Nodo nodo= NULL;
	
	if (a==NULL)
	  return(FALSO);
	
	if (a->raiz!=NULL)
	  nodo= buscarDatoRecursivo(a->raiz, dato);
	  
	if (nodo==NULL)
	  return(FALSO);    
	
	return(VERDADERO);
}

Nodo buscarDatoRecursivo(Nodo central, int dato)
{
	Nodo localizado=NULL;
	
	if (central==NULL)
	  return(NULL);
	  
	if (central->dato==dato)
	  return(central);
	  
	if (dato<central->dato)
	  {
	    localizado= buscarDatoRecursivo(central->enlaceIzq, dato);
	  }    
	  
	if (dato>central->dato)
	  {
	    localizado= buscarDatoRecursivo(central->enlaceDer, dato);
	  }    
	
	return(localizado);  
}

Nodo buscarMinimo(Nodo central)
{
	Nodo min= NULL;
	
	if (central==NULL)
	  return(NULL);
	  
	min= central;
	
	while (min->enlaceIzq!=NULL)
	     min= min->enlaceIzq;

	return(min);	
}

Nodo buscarMaximo(Nodo central)
{
	Nodo max= NULL;
	
	if (central==NULL)
	  return(NULL);
	  
	max= central;
	
	while (max->enlaceDer!=NULL)
	     max= max->enlaceDer;

	return(max);	
}

int eliminarDato(Arbol a, int dato)
{
	int sw= FALSO;
	
	if (a==NULL)
	  return(FALSO);
	
	if (a->raiz!=NULL)
	  sw= eliminarDatoRecursivo(a->raiz, dato);
	
	return(sw);
}

int eliminarDatoRecursivo(Nodo central, int dato)
{
	Nodo localizado=NULL;
	Nodo eliminar=NULL, eIzq= NULL, eDer= NULL;
	Nodo cIzq= NULL, cDer= NULL;
	Nodo max= NULL, min= NULL;
	int sw= FALSO;
	
	if (central==NULL)
	  return(FALSO);

    cIzq= central->enlaceIzq;
    cDer= central->enlaceDer;
    
    printf("%d\n", central->dato);
	
	if (cIzq!=NULL)
	  if (dato==cIzq->dato)  
	  {
	  	eliminar= cIzq;
	  	eIzq= eliminar->enlaceIzq;
	  	eDer= eliminar->enlaceDer;
	  	
	  	if (eIzq!=NULL)
	  	  {
	  	    max= buscarMaximo(eIzq);
	  	    max->enlaceDer= eDer;
	  	    central->enlaceIzq= eIzq;
	  	  }
	  	else
	  	  central->enlaceIzq= eDer;
	  	
	  	destruirNodo(eliminar);
	  	
	  	return(VERDADERO);
	  }

    if (cDer!=NULL)
	  if (dato==cDer->dato)  
	  {
	  	eliminar= cDer;
	  	eIzq= eliminar->enlaceIzq;
	  	eDer= eliminar->enlaceDer;
	  	
  	    if (eDer!=NULL)
	  	  {
	  	    min= buscarMinimo(eDer);
	  	    min->enlaceIzq= eIzq;
	  	
	  	    central->enlaceDer= eDer;
	  	  }
	  	else
	  	  central->enlaceDer= eIzq;
	  	
	  	destruirNodo(eliminar);
	  	
	  	return(VERDADERO);
	  }	  
	
	if (dato<central->dato)
	  {
	    sw= eliminarDatoRecursivo(central->enlaceIzq, dato);
	    if (sw==VERDADERO)
	      return(VERDADERO);
	  }    
	  
	if (dato>central->dato)
	  {
	    sw= eliminarDatoRecursivo(central->enlaceDer, dato);
	    if (sw==VERDADERO)
	      return(VERDADERO);	    
	  }    
	
	return(sw);  
}

int recorrerArbolEnOrden(Arbol a)
{
	if (a==NULL)
	  return(FALSO);
	  
	if (a->raiz==NULL)
	  return(FALSO);
	  
	recorrerNodosEnOrden(a->raiz);
	
	printf("\n");
	
	return(VERDADERO);	  
}

void recorrerNodosEnOrden(Nodo central)
{
	if (central==NULL)
	  return;
	  
	recorrerNodosEnOrden(central->enlaceIzq);
	printf("%d ", central->dato);
	recorrerNodosEnOrden(central->enlaceDer);
}

int recorrerArbolPreOrden(Arbol a)
{
	if (a==NULL)
	  return(FALSO);
	  
	if (a->raiz==NULL)
	  return(FALSO);
	  
	recorrerNodosPreOrden(a->raiz);
	
	printf("\n");
	
	return(VERDADERO);	  
}

void recorrerNodosPreOrden(Nodo central)
{
	if (central==NULL)
	  return;

	printf("%d ", central->dato);	  
	recorrerNodosPreOrden(central->enlaceIzq);
	recorrerNodosPreOrden(central->enlaceDer);
}

int recorrerArbolPostOrden(Arbol a)
{
	if (a==NULL)
	  return(FALSO);
	  
	if (a->raiz==NULL)
	  return(FALSO);
	  
	recorrerNodosPostOrden(a->raiz);
	
	printf("\n");
	
	return(VERDADERO);	  
}

void recorrerNodosPostOrden(Nodo central)
{
	if (central==NULL)
	  return;
	  
	recorrerNodosPostOrden(central->enlaceIzq);	
	recorrerNodosPostOrden(central->enlaceDer);
	printf("%d ", central->dato);
}

int recorrerArbolEnOrdenDescendente(Arbol a)
{
	if (a==NULL)
	  return(FALSO);
	  
	if (a->raiz==NULL)
	  return(FALSO);
	  
	recorrerNodosEnOrdenDescendente(a->raiz);
	
	printf("\n");
	
	return(VERDADERO);	  
}

void recorrerNodosEnOrdenDescendente(Nodo central)
{
	if (central==NULL)
	  return;
	  
	recorrerNodosEnOrdenDescendente(central->enlaceDer);
	printf("%d ", central->dato);
	recorrerNodosEnOrdenDescendente(central->enlaceIzq);
}
