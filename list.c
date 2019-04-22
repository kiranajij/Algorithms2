# include <stdio.h>
#include <stdlib.h>

typedef struct list{
	int item;
	struct list *next;
} list;

list *searchList(list *l, int x){
	if (l == NULL) return NULL;
	if (l->item == x){
		return l;
	} else {
		return searchList(l->next, x);
	}
}

int main(){
	int arr[] = {1, 5, 3, 6, 2, 7};
	int len = 6;
	list first = {arr[0], (list*) malloc(sizeof(list))};

	list* curr = (first.next);
	for (int i=1; i<len; i++){
		curr->item = arr[i];
		
		if (i == len-1){
			curr->next = NULL;
		} else {
			curr->next = (list*) malloc(sizeof(list));
			curr = curr->next;
		}
	}
	
	// curr = &first;
	// while(curr->next != NULL){
	// 	printf("%d\n", curr->item);
	// 	curr = (curr->next);
	// }

	list* sr = searchList(&first, 2);
	printf("%d\n", sr->item);
}