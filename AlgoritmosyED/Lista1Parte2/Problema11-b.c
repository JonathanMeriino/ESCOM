//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include<stdio.h>

//Algoritmo por burbuja 

void mostrarLista(int *);
#define SIZE 9

int main(int argc, char** argv){

	int lista[SIZE]={8,4,1,6,0,3,25,7,9};
	int n, l=SIZE,i,temp;

	mostrarLista(lista);


	do{
		n=0;
		//Recorrer la lista
		for(i=1;i<l;i++){
			//Verificar si los dos valores estan ordenados
			if(*(lista+i-1)>*(lista+i)){
				//Ordenar si es necesario
				temp=*(lista+i-1);
				*(lista+i-1)=*(lista+i);
				*(lista+i)=temp;
				n=i;
				mostrarLista(lista);
			}
		}
		l=n;
	}	while(n!=0);
	
}

//Función para mostrar estado de la lista

void mostrarLista(int *a){
  int i;
  for(i=0;i<SIZE;i++) printf("\t[%d]", *(a+i));
  printf("\n");
}


