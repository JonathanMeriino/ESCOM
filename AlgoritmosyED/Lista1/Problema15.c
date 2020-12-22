//Analice el comportamiento del siguiente codigo recursivo 
#include <stdio.h>
#include <stdlib.h>

void arbolBinario(int nivel,int nodo,int limite);
void arbolBaseB(int nivel,int nodo, int limite, int base );

void main(){
    int N=0, n=0,lim =4,base=3;
    arbolBinario(N,n,lim);
    arbolBaseB(N,n,lim,base);
           }
void arbolBinario(int nivel,int nodo,int limite){
    int k=0;
    if (nivel>=limite)
      return;

    for(k=0;k<nivel;k++)
        printf("\t");
    printf("nivel=%d,nodo=%d\n",nivel,nodo );

    arbolBinario(nivel+1,2+nodo+0,limite);
    arbolBinario(nivel+1,2+nodo+1,limite);
  }
  void arbolBaseB(int nivel,int nodo,int limite,int base){
      int k=0;
      if(nivel>=limite)
        return;
      for(k=0;k<nivel;k++)
          printf("\t");
      printf("nivel=%d,nodo=%d\n",nivel,nodo);

      for(k=0;k<base;k++)
            arbolBaseB(nivel+1,base*nodo+k,limite,base);
  }
