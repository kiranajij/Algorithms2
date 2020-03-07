# include <stdio.h>
# include <stdlib.h>

# define MAXSIZE 100

int partitionCache[MAXSIZE];
int i;


int nPartition(int n){
    /*
    This is the function to calculate the number of partition of a set which has
    'n' elements. It does it by a recursive relation defined by---
    
        P(n) := ways of partitioning a set with n elements.
        then P(n+1) will be calculated by

            P(n+1) = 1 + P(1) + P(2) + ... + P(n)
            P(1) = 1
            P(2) = 1 + 1 = 2
            P(2) = 1 + P(1) + P(2) = 1 + 1 + 2 = 4
            And so on.
    */

   int i, sum;


   if (partitionCache[n] <= 0){
        sum = 1;
        for (i=1; i<n; i++){
            sum += nPartition(i);
        }
        partitionCache[n] = sum;
   }

   return partitionCache[n];

}

void main(){
    int i;

    for (i=0; i<MAXSIZE; i++) partitionCache[i] = NULL;

    for (i=1; i<20; i++){
        int p = nPartition(i);
        printf("%d:\t%d\n", i, p);
    }
}