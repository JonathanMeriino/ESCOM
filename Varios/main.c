#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

#define NODO struct nodo
#define ARISTA struct arista
#define LIST struct pila 

//NODO
NODO {
    char dato;
    NODO *siguiente;
    ARISTA *adyacente;
    int visitado , terminado;  
    char anterior;
};
//ARISTA
ARISTA {
    NODO *vertice;
    ARISTA *siguiente;

};
//listas
LIST {
    NODO *dato; 
    LIST *siguiente;
};

NODO *start = NULL;
LIST *ini = NULL; 
LIST *final = NULL; 
void presentacion();
void insertarNodo(); 
void insertarAristas();
int main(){
    int N ; //numero de nodos 

    setLocale(LC_ALL,"");
    presentacion();

    printf("Ingrese el numero de nodos: ");
    scanf("%d",&N);

    for(int i=0; i<N; i++){
        //insertar nodo
        insertarNodo();

    }
    return 0;
}
void insertarAristas(){
    char ini,fin;

    ARISTA *nuevo =(ARISTA *)malloc(sizeof(ARISTA));
    nuevo->siguiente = NULL;
    NODO *aux;
    NODOD *aux2; 

    if(inicio==NULL)
    {
        printf("El grafo esta vacio");
        fflush(stdin);
        printf("Ingresa el nodo inicial y final: ");
        scanf("%c %c", &ini, &final);
        aux=inicio;
        aux2 = inicio;

        while(aux2 != NULL){
            if(aux2->dato==fin)
                break;
            
            aux2 = aux2->siguiente;

        }
        if(aux2 != NULL)
    }
    
}
void insertarNodo(){
    NODO *aux; 
    NODO *nuevo = (NODO*)malloc(sizeof(NODO));

    fflush(stdin);

    printf("Ingrese el nodo: ");
    scanf("%c",&nuevo->dato);

    nuevo->siguiente = NULL;
    nuevo->adyacente = NULL;
    nuevo->visitado =  nuevo->terminado =0;
    nuevo->anterior=0; 

    if(inicio == NULL)
        inicio = nuevo ;
    else{
        aux = inicio; 
        while(aux ->siguiente != NULL){
            aux = aux ->siguiente;
        }
        aux->siguiente = nuevo;
    }

}

void presentacion(){

}