#include <stdio.h>

int  main(int argc, char const *argv[]) {
  char *arr=NULL;
  char *cadena=NULL;
  int N=26, M=100, k=0,q;
  char letra='A';

  arr=(char*)malloc((N+1)*sizeof(char));

  for(k=0;k<N;k++)
      arr[k] = letra+k;
  arr[26]='\0';         //Fin de linea

  for(k=0;k<N;k++)
        printf("%c\n",arr[k] );
    printf("%s\n",arr );

  for (q=0,k=0;k<N;k+=2,q++)
        cadena[q] = arr[k];
  cadena[q] = '\0';
  printf("%s\n",cadena);

  for(q=0,k=N-1;k>=0;k-=6,q++)
      cadena[q]= arr[k];
  cadena[q]= '\0';
  printf("%s\n",cadena);

  for(q=0;q<N;q++)
      arr[q] = arr[q+1]:
  printf("%s\n",arr);

  return 0;
}
