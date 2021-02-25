#ifndef cola_h
#define cola_h

#include <stdio.h>
#include "pedido.h"

typedef struct NodoPedido
{
    Pedido *pedido;
    struct NodoPedido* siguiente;
    /* data */
}NodoPedido;
typedef struct Cola
{
    NodoPedido* primer;
    NodoPedido* ultimo;
}Cola;

NodoPedido* CrearNodo(Pedido* pedido);
void DestruirNodo(NodoPedido* nodo);

Cola* CrearCola();
void DestruirCola(Cola* cola);

void Encolar(Cola* cola,Pedido* pedido);
Pedido* consultar(Cola* cola);
void Eliminar(Cola* cola);





#endif