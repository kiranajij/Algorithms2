#include <stdio.h>

int binary_search(int s[], int key, int low, int high){
	int middle;
	if (low > high) return -1;
	middle = (low+high)/ 2;
	if (s[middle] == key) return middle;
	else if (s[middle] > key) return binary_search(s, key, low, middle-1);
	else return binary_search(s, key, middle+1, high);
}

int main(){
	int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
	int index = binary_search(arr, 10, 0, 14);
	printf("%d\n", index);
}