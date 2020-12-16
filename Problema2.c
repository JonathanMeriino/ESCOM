#include <stdio.h>
#include <stdlib.h>

int realizarAcrobacias(int x,int *q,int y,int *p,int *w){
  int k=0,c=0;

  for (k=0; k<x; k+=*w)
     {
        c=0;
        while (1) {
          if (c<y)
            break;
          if(k%2==0)
            *q+=k;
          else
              *p+=k;
          c++;

        }
     }
  x=-600;
  return(y-x);
}
void main() {
  int a=100,b=100, c=6,alpha=6, omega=7,delta=3;
  b=realizarAcrobacias(a,&alpha,c,&omega,&delta);
  printf("a=%d,b=%d,c=%d\n",a,b,c);
  printf("alpha=%d\n",alpha);
  printf("beta=%d\n",beta );
  printf("delta =%d\n",delta );

}
