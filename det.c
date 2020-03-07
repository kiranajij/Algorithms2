# include <stdio.h>
# include <stdlib.h>
# define MAXSIZE 10


float mat[MAXSIZE+1][MAXSIZE+1];

int sgn(int n){
    return (n%2==0)? 1:-1;
}

void main(){
    int n, i, j;      /* Dimenstion of the matrix */
    float fact;         /* dummy */
    float det;
    float sum1, sum2;   /* to hold the sums */

    printf("Enter the dimension of the matrix\t");
    scanf("%d", &n);

    if (n>MAXSIZE){
        perror("Size if greater than expected\n");
        exit(-1);
    }
    printf("Enter your matrix row by row\n");

    for(i=1; i<=n; i++){
        for (j=1; j<=n; j++){
            scanf("%f", &mat[i][j]);
        }
    }

    // printf("matrix has been scanned sucessfully %f", mat[1][1]);


    sum1 = 0;
    for (i=0; i<n ; i++){
        fact = 1;
        for (j=1; j<=n ; j++){
            fact *= mat[j][(i+j-1)%n + 1];
            // printf("%d, %d\n", j, (i+j-1)%n + 1);
        }
        sum1 += fact;
    }

    sum2 = 0;
    for (i=0; i<n; i++){
        fact = 1;
        for(j=1; j<=n; j++){
            int k = ((n+1-j-i)<=0)?(n+1-j-i+n):(n+1-i-j);
            //printf("%d,%d\n", j, k);
            fact *= mat[j][k];
        }
        sum2 += fact;
    }

    det = sum1- sum2;
    printf("Determinant = %f", det);
}


