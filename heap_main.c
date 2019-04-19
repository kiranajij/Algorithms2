# include <stdio.h>
# include "pq.h"

int main(){
	printf("FUCKYOUALL\n");
	priority_queue q = {};
	int arr[] = {1 , 2, 12, 32, 53, 12, 49, 53, 10, 85, 31, 15};
	heapsort(arr, 12);
	for (int i=0; i<12; i++){
		printf("%d\n", arr[i]);
	}
}