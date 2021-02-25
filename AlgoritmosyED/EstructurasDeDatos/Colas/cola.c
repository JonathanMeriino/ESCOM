#include "cola.h"

#include<stdlib.h>

NodoPedido* CrearNodo(Pedido* pedido)
{
    NodoPedido* nodo = (NodoPedido *)malloc(sizeof(NodoPedido));
    nodo->pedido = pedido;
    nodo ->siguiente = NULL;
    return nodo;
}
void DestruirNodo(NodoPedido* nodo)
{
    nodo ->pedido=NULL;
    nodo ->siguiente =NULL;
    free(nodo);

}

Cola* CrearCola()
{   
    Cola* cola = (Cola*)malloc(sizeof(Cola));
    cola->primer = cola->ultimo = NULL;
    return cola;
}
void DestruirCola(Cola* cola)
{
    while (cola->primer)
    {
        Eliminar(cola);
    }
    free(cola);

}
void Encolar(Cola* cola, Pedido* pedido)
{
    NodoPedido* nodo = CrearNodo(pedido);
    if(!cola->primer){
        cola->primer = nodo;
        cola->ultimo =nodo;
    }else {
        cola->ultimo->siguiente=nodo;
        cola->ultimo = nodo;
    }
}
Pedido* Consultar(Cola* cola)
{
    if(cola->primer){
        return cola->primer->pedido;
    }else{
        return NULL;
    }

}
void Eliminar(Cola* cola)
{
    if(cola->primer){
        NodoPedido* eliminado = cola ->primer;
        cola->primer = cola->primer->siguiente;
        DestruirNodo(eliminado);

        if(!cola->primer)
            cola->ultimo = NULL;
    }
}