
#include <stdio.h>
#include <stdlib.h>
#define Nodo struct nodo
#define Arista struct arista

Nodo{
    char dato;
    Nodo *siguiente;
    Arista *adyacencia;
};
Arista{
    Nodo *vrt;
    Arista *siguiente;
};

Nodo *inicio = NULL;


void insertarNodo(){
    Nodo *aux;
    Nodo *nuevo = (Nodo*)malloc(sizeof(Nodo));
    fflush(stdin);
    printf("Ingrese vertice:");
    scanf("%c",&nuevo->dato);

    nuevo->siguiente=NULL;
    nuevo->adyacencia =NULL;

    if(inicio==NULL){
        inicio =nuevo;
    }else{
        aux=inicio;
        while(aux->siguiente!=NULL){
            aux=aux->siguiente;
        }
        aux->siguiente =nuevo;
    }
}
void agregarArista(Nodo *aux,Nodo *aux2,Arista *nuevo){
    Arista *a;

    if(aux->adyacencia==NULL){
        aux->adyacencia=nuevo;
        nuevo->vrt=aux2;
    }else{
        a=aux->adyacencia;
        while (a->siguiente!=NULL)
            a=a->siguiente;
        nuevo->vrt=aux2;
        a->siguiente=nuevo;
    }
}
void insertarArista(){
    char ini,fin;
    Arista *nuevo = (Arista*)malloc(sizeof(Arista));
    Nodo *aux, *aux2;

    if(inicio==NULL){
        printf("Erros: el grafo esta vacio");
        return;
    }
    fflush(stdin);
    printf("Ingresar el nodo inicial y final");
    scanf("%c %c", &ini, &fin);
    aux=inicio;
    aux2=inicio;

    while(aux2!=NULL){
        if (aux2->dato==fin)
            break;
        aux2=aux2->siguiente;

    }
    if (aux2==NULL){
        printf("Error: Vertice no se encontro \n");
        return;
    }
    while(aux!=NULL){
        if(aux->dato==ini){
            agregarArista(aux,aux2,nuevo);
            return; 
        }
        aux2=aux->siguiente;
    }
    if(aux2==NULL){
        printf("Error: vertice no encontrado\n");
        return;
    }
}
void menu(){

int opcion,N,i;
    printf("Ingrese el numero de vertices: ");
    scanf("%i",&N);

    for(i=0; i<N; i++){
        insertarNodo();
    }
    system("cls");
    do{
        printf("-----------------\n");
        printf("1. Insertar Vertice \n");
        printf("2. Insertar Arista \n");
        printf("3. Salir\n");
        printf("-----------------\n");
        printf("Escoge una opcion: ");
        scanf("%i",&opcion);

        switch(opcion){
            case 1: insertarNodo(); break;
            case 2: insertarArista();break;
            case 3: break;
            default: printf("No existe");

        }
        system("cls");
    }while(opcion!=3);
    
}
int main(int argc, char const *argv[])
{
  menu();  
}