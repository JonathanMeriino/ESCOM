//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 
#include <stdio.h> 
#include <math.h> 

int busquedaBinariaIterativa(int arreglo[], int busqueda, int izquierda, int derecha);
int veces=0;

int main(){
	
    int numeros[] = {1,2, 4, 16, 28, 29, 33, 40, 52, 54, 55, 58, 59, 64, 65, 75, 83, 89, 90, 94, 95};
    int busqueda; 
    printf("\n Numero buscado:\n");
	scanf("%d",&busqueda);
    int longitudDelArreglo = sizeof(numeros) / sizeof(numeros[0]);
    int resultadoBusquedaIterativa = busquedaBinariaIterativa(numeros, busqueda, 0, longitudDelArreglo - 1);
    printf("Al buscar %d iterativamente, el resultado es %d\n", busqueda, resultadoBusquedaIterativa);
    printf("veces: %d", veces);
    
    return 0;
}

int busquedaBinariaIterativa(int arreglo[], int busqueda, int izquierda, int derecha)
{
	if (izquierda > derecha) return -1;
    veces++; 

    int indiceDeLaMitad = floor((izquierda + derecha) / 2);
	int valorQueEstaEnElMedio = arreglo[indiceDeLaMitad];
    if (busqueda == valorQueEstaEnElMedio){
        return indiceDeLaMitad;
        veces++; 
    }
    
	if (busqueda < valorQueEstaEnElMedio){
        // Entonces está hacia la izquierda
        derecha = indiceDeLaMitad - 1;
        veces++; 
    }
	else{
        // Está hacia la derecha
        izquierda = indiceDeLaMitad + 1;
        veces++; 
    } 
	return busquedaBinariaIterativa(arreglo, busqueda, izquierda, derecha);
}

