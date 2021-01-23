#include<stdio.h>
#include<math.h>
 
int tablero[20],cuenta;
 
int main()
{
 int n,i,j;
 void reina(int row,int n);
 
  printf("\n\nNumero de reinas:");
 scanf("%d",&n);
 reina(1,n);
 return 0;
}

void print(int n)
{
 int i,j;
 printf("\n\n Solucion %d:\n\n",++cuenta);
 
 for(i=1;i<=n;++i)
  printf("\t%d",i);
 
 for(i=1;i<=n;++i)
 {
  printf("\n\n%d",i);
  for(j=1;j<=n;++j) 
  {
   if(tablero[i]==j)
    printf("\tQ"); 
   else
    printf("\t-");
  }
 }
}
 
/*funtion to check conflicts
If no conflict for desired postion returns 1 otherwise returns 0*/
int desplazamiento(int fila,int columna)
{
 int i;
 for(i=1;i<=fila-1;++i)
 {
  //checking column and digonal conflicts
  if(tablero[i]==columna)
   return 0;
  else
   if(abs(tablero[i]-columna)==abs(i-fila))
    return 0;
 }
 
 return 1; //no conflicts
}
 
//function to check for proper positioning of queen
void reina(int fila,int n)
{
 int columna;
 for(columna=1;columna<=n;++columna)
 {
  if(desplazamiento(fila,columna))
  {
   tablero[fila]=columna; //no conflicts so place queen
   if(fila==n) //dead end
    print(n); //printing the board configuration
   else //try queen with next position
    reina(fila+1,n);
  }
 }
}
