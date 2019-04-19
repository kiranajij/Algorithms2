# include <stdio.h>
# include <stdlib.h>

void swap(int[], int, int);
void insertsionsort(int[], int);
void parray(int[], int);
int intcomp(const void*, const void*);

void insertsionsort(int arr[], int n){
	int i, j;		// counters
	for (i=1; i< n; i++){
		j=i;
		while(j > 0 && arr[j] < arr[j-1]){
			swap(arr, j, --j);
			// j--;
		}
	}
}

void swap(int arr[], int i, int j){
	int tmp = arr[j];
	arr[j] = arr[i];
	arr[i] = tmp;
}

void parray(int arr[], int n){
	for (int i=0; i<n; i++) printf("%d ", arr[i]);
	printf("\n");
}

int main(){
	int arr[] = {5, 3, 1, 2, 23, 64, 23, 53, 64, 12, 54, 23, 56, 98,64};
	parray(arr, 15);
	// insertsionsort(arr, 15);
	qsort(arr, 15, sizeof(int), &intcomp);
	parray(arr, 15);
	return 1;
}

int intcomp(const void *a, const void *b){
	int x = *(int*)a, y = *(int*)b;
	if (x > y) return -1;
	else if (x < y) return 1;
	else return 0;
}

void _0x123(int _0x1){
	printf("%d\n", _0x1);
}