//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include<stdio.h>

//Algoritmo por inserción
#define N 9
void mostrarLista(int*);

int main(int argc, char** argv){
	int arreglo[N]={8,4,1,6,0,3,25,7,9};
	int i,clave,j;
   //Recorrer el arreglo
	for (i = 1; i < N; i++){	   
		clave = *(arreglo+i);
		j = i-1;
		//Comparar el valor selecionado con todos los valores anteriores
		while (j >= 0 && *(arreglo+j) > clave){
			//Insertar el valor donde corresponda
			*(arreglo+j+1) = *(arreglo+j);
			j = j-1;
		}
		*(arreglo+j+1) = clave;
		mostrarLista(arreglo);
	}    
	mostrarLista(arreglo);  
	
	return 0;
}

//Función para mostrar estado de la lista
void mostrarLista(int *lista){
	int i;
	for (i=0; i< N; i++){
		printf("%d ",*(lista+i));
	}
	printf("\n");;
}
