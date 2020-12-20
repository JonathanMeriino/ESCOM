#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VERDADERO	1
#define FALSO		0

typedef struct memoria
{
	int *arr;
	int longitud;
} t_memoria, *Memoria;

Memoria crearMemoria(int N);
int construirMemoria(Memoria *M, int N);
int destruirMemoria(Memoria m);
int escribirDato(Memoria m, int dato, int dir);
int leerDato(Memoria m, int *dato, int dir);
int desplegarMemoria(Memoria m);
int ordenarMemoria(Memoria m);
int desordenarMemoria(Memoria m);
int ordenarMemoria(Memoria m);
int buscarDato(Memoria m, int dato, int *dir);

int main(int argc, char *argv[])
{
	Memoria m= NULL;
	int x=0, N=100;
	int sw= FALSO;
	int k=0;
	
	//m= crearMemoria(N);
	srand(time(NULL));
	
	sw= construirMemoria(&m, N);
	
	if (sw==VERDADERO)
		{
			for (k=0; k<N; k++)
				{
					x= rand()%100;
					sw= escribirDato(m, x, k);
				}
				
			for (k=0; k<N; k++)
				{
					sw= leerDato(m, &x, k);
					printf("%d\t", x);					
				}				
			printf("\n");
			
			desplegarMemoria(m);
			
			ordenarMemoria(m);
			desplegarMemoria(m);
			desordenarMemoria(m);
			desplegarMemoria(m);
			
			printf("buscar dato: ");
			scanf("%d", &x);
			buscarDato(m, x, &k);
			printf("El dato %d está en %d\n", x, k);
			
			destruirMemoria(m);
		}
	
	return 0;
}

Memoria crearMemoria(int N)
{
	Memoria m= NULL;
	
	if (N>0)
		{
			m= (Memoria) malloc(sizeof(t_memoria));
			
			if (m!=NULL)	
				{
					m->arr= (int *) malloc(N*sizeof(int));
					m->longitud= N;
				}
		}
		
	return(m);
}

int construirMemoria(Memoria *M, int N)
{
	Memoria m= NULL;
	
	if (N>0)
		{
			m= (Memoria) malloc(sizeof(t_memoria));
			
			if (m!=NULL)	
				{
					m->arr= (int *) malloc(N*sizeof(int));
					if (m->arr!=NULL)
					  {					  
						m->longitud= N;
						*M= m;
						return(VERDADERO);
					  }
				}
		}
	
	return(FALSO);
}

int destruirMemoria(Memoria m)
{
	if (m!=NULL)
		{
			if (m->arr!=NULL)
				{
					free(m->arr);
				}
			free(m);
			return(VERDADERO);
		}
	return(FALSO);
}

int escribirDato(Memoria m, int dato, int dir)
{
	if (m!=NULL)
		{
			if (m->arr!=NULL && dir>=0 && dir<m->longitud)	
				{
					m->arr[dir]= dato;
					return(VERDADERO);
				}
		}
	return(FALSO);
}

int leerDato(Memoria m, int *dato, int dir)
{
	if (m!=NULL)
		{
			if (m->arr!=NULL && dir>=0 && dir<m->longitud)	
				{
					*dato= m->arr[dir];
					return(VERDADERO);
				}
		}
	return(FALSO);
}

int desplegarMemoria(Memoria m)
{
	int k=0;
	
	if (m!=NULL)
		{
			if (m->arr!=NULL)
				{
					for (k=0; k<m->longitud; k++)
					   printf("%d\t", m->arr[k]);
					printf("\n");
					return(VERDADERO);
				}
		}

	return(FALSO);
}

int buscarDato(Memoria m, int dato, int *dir)
{
	int k=0;
	
	if (m!=NULL)
		{
			if (m->arr!=NULL)
				{
					for (k=0; k<m->longitud; k++)	
					   if (m->arr[k]==dato) 
					     {
					     	*dir= k;
					     	return(VERDADERO);
						 }
				}
		}
		
	return(FALSO);
}


int desordenarMemoria(Memoria m)
{
	int k=0, salto=0, aux=0;
	
	if (m!=NULL)
		{
			if (m->arr!=NULL)
				{
					for (k=0; k<m->longitud; k++)
						{
							salto= rand()%m->longitud;
							
							aux= m->arr[salto];
							m->arr[salto]= m->arr[k];
							m->arr[k]= aux;
						}
					return(VERDADERO);
				}
		}
	return(FALSO);
}

int ordenarMemoria(Memoria m)
{
	int i=0, j=0, aux=0;
	
	if (m!=NULL)	
		{
			if (m->arr!=NULL)
				{
					for (i=0; i<m->longitud; i++)
						for (j= i+1; j<m->longitud; j++)
						   {
						   		if (m->arr[j]<m->arr[i])
						   			{
						   				aux= m->arr[j];
						   				m->arr[j]= m->arr[i];
						   				m->arr[i]= aux;
									}
						   }
					return(VERDADERO);
				}
		}
	return(FALSO);
}


