# include <stdio.h>

void quicksort(int[], int, int);
int partition(int[], int, int);

void quicksort(int s[], int l, int h){
	int p;
	if(h>l){
		p = partition(s, l, h);
		quicksort(s, l, p-1);
		quicksort(s, p+1, h);
	}
}

void swap(int* a, int* b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int partition(int s[], int l, int h){
	int i, pivot=h, divpos=l;
	for (i=l; i<h; i++){
		if(s[i] < s[pivot]) swap(&s[i], &s[divpos++]);
	}
	swap(&s[divpos], &s[pivot]);
	return divpos;
}

void parray(int* arr, int n){
	for (int i=0; i<n; i++) printf("%d ", arr[i]);
	printf("\n");
}


int main(){
	int a[] = {1, 3, 6, 7, 8 ,2 ,5, 4};
	parray(a, 8);
	// partition(a, 0, 7);
	// parray(a, 8);
	quicksort(a, 0, 7);
	parray(a, 8);
}