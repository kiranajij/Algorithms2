
#include <stdio.h>
#include <stdlib.h>

int repeat=0;

int is_solution(int a[], int k, int n, int sum){
    return (n == k);
}
void print_arr(int arr[], int start, int end){
    for (int i=start; i<=end; i++) {printf("%d ", arr[i]);}
    printf("\n");
}
void process_solution(int a[], int k, int n, int sum){
    if (sum != 0) return;
    print_arr(a, 1, k);
}
int generate_candidates(int arr[], int k, int n, int sum, int cand[]){
    int n_cand = 0;
    for (int i=1; i<=6; i++){
        /*
        * uncommenting first one will give you all the
        * possible results.
        * the second one print one combination only once.
        * so if "1 1 2" gets printed, "2 1 1" or "1 2 1" will
        * not get printed
        */
        //if(i<=sum)
        int s = (i<=sum);
        int a = (i>=arr[k-1]);
        int r= !repeat;
        int cond = s && (((!a) && (!r)) || a);
        if (cond)
        {
            cand[n_cand] = i;
            n_cand++;
        }
    }
    return n_cand;
}
int run(int a[], int k, int n, int sum){
    if (is_solution(a, k, n, sum)){
        process_solution(a, k, n, sum);
    } else {
        k++;
        int cand[6];
        int n_cand = generate_candidates(a, k, n, sum, cand);
        for (int i=0; i<n_cand; i++){
            a[k] = cand[i];
            run(a, k, n, sum-a[k]);
        }
    }
}

int main(int argc, char* argv[]){
    int n, sum;
    if (argc != 4){
        char c = 'x';
        printf("dice -n -sum\n");
        printf("Please input number of dices:\t");
        scanf("%d", &n);
        printf("Please input desired sum:\t");
        scanf("%d", &sum);
//        printf("Please enter y for repetition n for no repetition:\t");
//        c = getchar();
//        printf("%c", c);
        if (c == 'y'|| c=='Y')
            repeat = 1;
        if (c=='n' || c == 'N') repeat = 0;
    } else {
        n = atoi(argv[1]);
        sum = atoi(argv[2]);
        char c = *argv[3];
        if (c == 'y'|| c=='Y')
            repeat = 1;
        if (c=='n' || c == 'N') repeat = 0;

    }
//    int n=3, sum=10;
    int a[30];
    run(a, 0, n, sum);
}
