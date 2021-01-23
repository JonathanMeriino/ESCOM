#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int k=0, x=0, i=0, j=0;
	int N=10;
	
	while ( k<N, k++)
		x+=k;
		printf("x=%d\n", x); 
		printf("k=%d\n", k);   
		
	printf("x primer=%d\n\n", x); 
	
	for (k=1, x=0; k<N; k*=6)
		x+=k; 
		printf("x=%d\n", x);
		printf("k=%d\n", k);
		
	printf("x=%d\n\n ", x);
	
	for (i=0, x=0; i<N; i+=2)
		for(j=0; j<N; j+=3)
			x+=i*j; 
			printf("x=%d\n", x);
			printf("j=%d\n", j);
		printf("i=%d\n", i);
		
			
	
	printf("x=%d\n\n", x);
	
	for (i=N, x=0; i>0; i/=2)
		for(j=N; j>0; j--)
			x+=i*j; 
			printf("x=%d\n", x);
			printf("j=%d\n", j);
		printf("i=%d\n", i);
			
	printf("x=%d\n\n", x);
}
