#include <stdio.h>

#define MAXSIZE 30
#define None -1
#define MAXINT 100000

int darray[MAXSIZE];
int helper[MAXSIZE];

void initialize(){
	for (int i=1 ;i<MAXSIZE; i++)
		darray[i] = None;
	darray[0] = 0;
}

void print_array(int* a, int n){
	printf("[");
	for (int i=0; i<n; i++){
		printf("%d ", a[i]);
	}
	printf("]\n");
}

void backtrack(int* a, int n, int* k){
	if (n == 0) return;
	a[*k] = helper[n];
	*k = *k+1;
	backtrack(a, n-a[*k-1], k);
}

int select_coins(int* coins, int size, int target)
{
	initialize();
	// for (int i=0;i<size; i++)
	// {
	// 	darray[coins[i]] = 1;
	// }

	for (int i=1; i<=target; i++)
	{
		int min_cost = MAXINT;
		for (int j=0; j<size; j++)
		{
			if (coins[j] <= i)
			{
				int this_cost = 1 + darray[i-coins[j]];
				if(this_cost < min_cost)
					min_cost = this_cost;
					helper[ i ] = coins[j];
			}
			darray[i] = min_cost;
		}
	}
	int a[MAXSIZE];
	int k=0;
	backtrack(a, target, &k);
	print_array(a, k);

	return darray[target];
}

void main(){
	int x;
	int coins[] = {1, 6, 10};
	while(1){
		scanf("%d", &x);
		int min = select_coins(coins, 3, x);
		printf("%d\n", min);
	}
}