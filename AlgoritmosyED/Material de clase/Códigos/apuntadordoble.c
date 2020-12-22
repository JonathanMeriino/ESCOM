#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
	int **d= NULL;
	int *p= NULL, *q= NULL;
	int x= 13, y=0;
	
	p= &x;
	d= &p;
	q= *d;
	y= *q;
	
	printf("y= %d\n", y);
	
	
	return 0;
}
