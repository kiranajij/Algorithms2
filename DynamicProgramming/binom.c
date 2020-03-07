# include <stdio.h>
# include <stdlib.h>

# define MAXSIZE 30
# define UNKNOWN -1

int binom[MAXSIZE][MAXSIZE];

void initialize_arr(int a[MAXSIZE][MAXSIZE], int size){
    int i, j;      /* counter */

    /*
     * Initialize Every value with UNKNOWN
    */
    for(i=0; i<size; i++){
        for (j=0; j<size; j++){
            a[i][j] = UNKNOWN;
        }
    }
}

void initialize_coeff(int a[MAXSIZE][MAXSIZE], int size){
    int i;       /* counter */

    /* Set the known values for every row,
     * That is C{n, 0} = 1 and C{n, n} = 1
    */
    for (i=0; i<size; i++){
        a[i][0] = 1;
        a[i][i] = 1;
    }
}

int get_binom(int n, int r){
    if (binom[n][r] == UNKNOWN){
        binom[n][r] = get_binom(n-1, r-1) +
                        get_binom(n-1, r);
    }

    return binom[n][r];
}

int main(){
    int n, r, ans;
    initialize_arr(binom, MAXSIZE);
    initialize_coeff(binom, MAXSIZE);
    while(1){
        printf("Enter n and r:\t");
        scanf("%d %d", &n, &r);
        ans = get_binom(n, r);
        printf("  %d\n", ans);
    }
}
