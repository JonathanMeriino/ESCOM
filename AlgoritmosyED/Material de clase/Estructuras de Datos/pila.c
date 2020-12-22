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


typedef struct pila
{
	Nodo base;
	Nodo tope;
	int longitud;
}	t_pila, *Pila;

int main(int argc, char *argv[])
{
	Pila p= NULL;
	Elemento e= NULL;
	int k=0, x=0;
	int N= 1000;	
	
	crearPila(&p);
	
	for (k=0; k<N; k++)
	 	{
	 		crearElemento(&e);
	 		escribirDato(e, k);
			insertarElemento(p, e);
		}
	
	for (k=0; k<N; k++)
	 	{
	 		quitarElemento(p, &e);
	 		leerDato(e, &x);
	 		printf("%d\n", x);
		}
	
	destruirPila(p);
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
	
	return(VERDADERO);
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

int crearPila(Pila *p)
{
	Pila q= NULL;
	
	q= (Pila) malloc(sizeof(t_pila));
	
	if (q==NULL)
	  return(FALSO);
	  
	q->base= NULL;
	q->tope= NULL;
	q->longitud= 0;
	
	*p= q;
	
	return(VERDADERO);
}


int insertarElemento(Pila p, Elemento e)
{
	Nodo n= NULL;
	int sw= FALSO;
	
	if (p==NULL)
	  return(FALSO);
	
	sw= crearNodo(&n);
	
	if (sw==VERDADERO)
		{
			sw= escribirElemento(n, e);
			if (sw==VERDADERO)
				{
					if (p->longitud==0)
					  p->base= n;
					else
					  conectarEnlaceA(n, p->tope);
					  
					p->tope= n;
					(p->longitud)++;
					return(VERDADERO);
				}
		}
		
	return(FALSO);
}

int quitarElemento(Pila p, Elemento *e)
{
	int sw= FALSO;
	Nodo abajo= NULL;
	
	if (p==NULL)
	  return(FALSO);
	  
	if (p->longitud==0)
	  return(FALSO);
	  
	sw= leerElemento(p->tope, e);
	
	if (sw==VERDADERO)
		{
			sw= consultarEnlaceA(p->tope, &abajo);			
			if (sw==VERDADERO)
				{				
					sw= desconectarEnlaceA(p->tope);
					if (sw==VERDADERO)
						{		
							sw= destruirNodo(p->tope);
							if (sw==VERDADERO)
								{	
									p->tope= abajo;
									(p->longitud)--;
							
									if (p->longitud==0)
							  			{
							  				p->tope= NULL;
							  				p->base= NULL;
							  			}
							  	}
							return(VERDADERO);
						}
				}
		}
		
	return(FALSO);
}

int consultarTope(Pila p, Elemento *e)
{
	int sw= FALSO;
	
	if (p==NULL)
	  return(FALSO);
	  
	if (p->longitud==0 || p->tope==NULL)
	  return(FALSO);
	  
	sw= leerElemento(p->tope, e);
	  
	return(sw);
}

int destruirPila(Pila p)
{
	Nodo aux= NULL;
	int sw= NULL;
	
	if (p==NULL)
	  return(FALSO);
	  
	while(p->tope!=NULL)
	{
		sw= consultarEnlaceA(p->tope, &aux);
		if (sw==FALSO)
		  return(FALSO);
		  
		sw= desconectarEnlaceA(p->tope);
		if (sw==FALSO)
		  return(FALSO);
		  
		sw= destruirNodo(p->tope);
		if (sw==FALSO)
		  return(FALSO);
		
		p->tope= aux;
		p->longitud--;
	}
	
	p->tope= NULL;
	p->base= NULL;
	free(p);
	
	return(VERDADERO);
}



