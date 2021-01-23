//Díaz Torres Laura Alma 
//Escuela Superior de Cómputo
//Ingenería en Inteligencia Artificial 

#include<stdio.h>
#include<stdlib.h>
#define N 9
//Algoritmo por mezcla 

int times=0; 

int main(){
    int i, vector[N] = {8,4,1,6,0,3,25,7,9};
 
    mezcla(vector,N);
 
    for(i=0;i<9;i++)
        printf("%i,\t", vector[i]);
 
    printf("veces: %d", times); 
	return 0;
}

void mezcla(int vector[], int n)
{
    int *vector1, *vector2, n1, n2,x,y;
    if (n>1)
    {
        if (n%2 == 0)
            n1=n2=(int) n / 2;
        else
        {
            n1=(int) n / 2;n2=n1+1;
        }
        vector1=(int *) malloc(sizeof(int)*n1);
        vector2=(int *) malloc(sizeof(int)*n2);
        for(x=0;x<n1;x++)
            vector1[x]=vector[x];
        for(y=0;y<n2;x++,y++)
            vector2[y]=vector[x];
        mezcla(vector1, n1);
        mezcla(vector2,n2);
        mezclar(vector1, n1, vector2, n2, vector);
        free(vector1);
        free(vector2);
    }      
}

void mezclar(int arreglo1[], int n1, int arreglo2[], int n2, int arreglo3[])
{
    int x1=0, x2=0, x3=0;
 
    while (x1<n1 && x2<n2) {
        if (arreglo1[x1]<arreglo2[x2]) {
            arreglo3[x3] = arreglo1[x1];
            x1++;
            times++; 
        } else {
            arreglo3[x3] = arreglo2[x2];
            x2++;
            times++; 
        }
        x3++;
        times++;
    }
    while (x1<n1) {
        arreglo3[x3] = arreglo1[x1];
        x1++;
        x3++;
        times++;
    }
    while (x2<n2) {
        arreglo3[x3] = arreglo2[x2];
        x2++;
        x3++;
        times++;
    }
}
 
