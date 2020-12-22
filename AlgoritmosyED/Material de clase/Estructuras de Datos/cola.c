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

typedef struct cola
{
	Nodo primero;
	Nodo ultimo;
	int longitud;
}	t_cola, *Cola;

int main(int argc, char *argv[])
{
	Cola c= NULL;
	Elemento e= NULL;
	int k=0, x=0;
	int N= 1000;	
	
	crearCola(&c);
	
	for (k=0; k<N; k++)
	 	{
	 		crearElemento(&e);
	 		escribirDato(e, k);
			insertarElemento(c, e);
		}
	
	for (k=0; k<N; k++)
	 	{
	 		quitarElemento(c, &e);
	 		leerDato(e, &x);
	 		printf("%d\n", x);
		}
	
	destruirCola(c);
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

int crearCola(Cola *c)
{
	Cola q= NULL;

	q= (Cola) malloc(sizeof(t_cola));

	if (q==NULL)
	  return(FALSO);

	q->primero= NULL;
	q->ultimo= NULL;
	q->longitud= 0;

	*c= q;

	return(VERDADERO);
}


int insertarElemento(Cola c, Elemento e)
{
	Nodo n= NULL;
	int sw= FALSO;
	
	if (c==NULL)
	  return(FALSO);
	
	sw= crearNodo(&n);
	
	if (sw==VERDADERO)
		{
			sw= escribirElemento(n, e);
			if (sw==VERDADERO)
				{
					if (c->longitud==0)
					  c->primero= n;
					else
					  conectarEnlaceA(c->ultimo, n);
					  
					c->ultimo= n;
					(c->longitud)++;
					return(VERDADERO);
				}
		}
		
	return(FALSO);
}

int quitarElemento(Cola c, Elemento *e)
{
	int sw= FALSO;
	Nodo siguiente= NULL;
	
	if (c==NULL)
	  return(FALSO);
	  
	if (c->longitud==0)
	  return(FALSO);
	  
	sw= leerElemento(c->primero, e);
	
	if (sw==VERDADERO)
		{
			sw= consultarEnlaceA(c->primero, &siguiente);			
			if (sw==VERDADERO)
				{				
					sw= desconectarEnlaceA(c->primero);
					if (sw==VERDADERO)
						{		
							sw= destruirNodo(c->primero);
							if (sw==VERDADERO)
								{	
									c->primero= siguiente;
									(c->longitud)--;
							
									if (c->longitud==0)
							  			{
							  				c->primero= NULL;
							  				c->ultimo= NULL;
							  			}
							  	}
							return(VERDADERO);
						}
				}
		}
		
	return(FALSO);
}

int consultarPrimero(Cola c, Elemento *e)
{
	int sw= FALSO;
	
	if (c==NULL)
	  return(FALSO);
	  
	if (c->longitud==0 || c->primero==NULL)
	  return(FALSO);
	  
	sw= leerElemento(c->primero, e);
	  
	return(sw);
}

int destruirCola(Cola c)
{
	Nodo aux= NULL;
	int sw= FALSO;
	
	if (c==NULL)
	  return(FALSO);
	  
	while(c->primero!=NULL)
	{
		sw= consultarEnlaceA(c->primero, &aux);
		if (sw==FALSO)
		  return(FALSO);
		  
		sw= desconectarEnlaceA(c->primero);
		if (sw==FALSO)
		  return(FALSO);
		  
		sw= destruirNodo(c->primero);
		if (sw==FALSO)
		  return(FALSO);
		
		c->primero= aux;
		c->longitud--;
	}
	
	c->primero= NULL;
	c->ultimo= NULL;
	free(c);
	
	return(VERDADERO);
}

