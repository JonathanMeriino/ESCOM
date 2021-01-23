#include <stdio.h>
#include <stdlib.h>

int ******crearHipercubo(int A, int B, int C, int D, int E, int F); 
void imprimirHipercubo(int ******hipercubo, int A, int B, int C, int D, int E, int F);
void destruirHipercubo(int ******hipercubo, int A, int B, int C, int D, int E, int F);


int main(int argc, char *argv[]){
	int ******hipercubo= NULL; 
	int A=3, B=4, C=5, D=6, E=7, F=8; 
	
	hipercubo= crearHipercubo(A, B, C, D, E, F); 
	imprimirHipercubo(hipercubo, A, B, C, D, E, F); 
	destruirHipercubo(hipercubo, A, B, C, D, E, F);
		
	return 0;
}

int ******crearHipercubo(int A, int B, int C, int D, int E, int F){
	int ******hipercubo= NULL; 
	int i=0, j=0, k=0, l=0, m=0, n=0; 
	
	hipercubo=(int ******) malloc(A*sizeof(int *****));
	
	for (i=0; i<A; i++)
	{
		hipercubo[i]= (int *****) malloc(B*sizeof(int ****));
		
		for (j=0; j<B; j++)
		{
			hipercubo[i][j]= (int ****) malloc(C*sizeof(int ***)); 
			
			for (k=0; k<C; k++)
			{
				hipercubo[i][j][k]= (int ***) malloc (D* sizeof(int **)); 
				
				for (l=0; l<D; l++)
				{
					hipercubo[i][j][k][l]= (int **) malloc(E* sizeof(int *)); 
					
					for (m=0; m<E; m++)
					{
						hipercubo[i][j][k][l][m]= (int *) malloc(F* sizeof (int)); 
						
						for (n=0; n<F; n++)
						{
							hipercubo[i][j][k][l][m][n]=i*j*k*l*m*n; 
						}
					}
				}
			}
		}
		
	}
	
	return(hipercubo); 
	
}

void imprimirHipercubo(int ******hipercubo, int A, int B, int C, int D, int E, int F){
    int i=0, j=0, k=0, l=0, m=0, n=0; 
    
    for(i=0; i<A; i++){
        printf("\nVolumen en 6 [%d]:\n", i); 
        for(j=0; j<B; j++){
            printf("\n\tVolumen en 5 [%d]:\n", j); 
            for(k=0; k<C; k++){
                printf("\n\t\tVolumen en 4 [%d]:\n", k); 
                for(l=0; l<D; l++){
                    printf("\n\t\t\tVolumen [%d]:\n", l); 
                    for(m=0; m<E; m++){
                        printf("\n\t\t\t\tRebanada [%d]:", m); 
                        for(n=0; n<F; n++){
                            printf("%d\t", hipercubo[i][j][k][l][m][n]); 
                        }
                    }
                } 
            }
        }
    }
}

void destruirHipercubo(int ******hipercubo, int A, int B, int C, int D, int E, int F){
	int i=0, j=0, k=0, l=0, m=0, n=0; 
	
	for (i=0; i<A; i++){		
		for(j=0; j<B; j++){
			for (k=0; k<C; k++){
				for (l=0; l<D; l++){
					for (m=0; m<E; m++){
						for (n=0; n<F; n++){
							free(hipercubo[i][j][k][l][m]);  
							
						}
						free(hipercubo[i][j][k][l]);
					}
					free(hipercubo[i][j][k]);
				}
				free(hipercubo[i][j]);
			}
			free(hipercubo[i]);
		}
		free(hipercubo);
	}
}

