
#include <stdio.h>
#include <stdlib.h>

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
int generate_candidates(int a[], int k, int n, int sum, int cand[]){
    int n_cand = 0;
    for (int i=1; i<=6; i++){
        if (i<=sum){
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

int main(){
    int n=3, sum=10;
    int a[30];
    run(a, 0, n, sum);
}