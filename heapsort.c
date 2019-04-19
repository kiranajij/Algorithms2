# include <stdio.h>
# include <stdlib.h>



# include "pq.h"



int pq_parent(int n){
	if (n==1) return (-1);
	else return ((int) n/2);
}

int pq_lchild(int n){
	return 2*n;
}

void pq_bubbleup(priority_queue *q, int i){
	int p_q = pq_parent(i);
	if (p_q != -1){
		if (q->q[p_q] > q->q[i]){
			pq_swap(q, p_q, i);
			pq_bubbleup(q, p_q);
		}
	}
}

void pq_insert(priority_queue *q, int item){
	if (q->n >= PQ_SIZE){
		printf("Warning: priority queue size overflow: %d\n", item);
	}
	else{
		q->n = q->n +1;
		q->q[q->n] = item;
		pq_bubbleup(q, q->n);
	}
}

void pq_init(priority_queue *q){
	q->n = 0;
}

void make_heap(priority_queue *q, int a[], int n){
	int i;

	pq_init(q);
	for (i=0; i<n; i++){
		pq_insert(q, a[i]);
	}
}

void pq_swap(priority_queue *q, int i_1, int i_2){
	int tmp = q->q[i_1];
	q->q[i_1] = q->q[i_2];
	q->q[i_2] = tmp;
}

int extract_min(priority_queue *q){
	int min = -1;

	if (q->n <= 0)	printf("Warning: Empty Priority queue\n");
	else {
		min = q->q[1];
		q->q[1] = q->q[q->n];
		q->n = q->n - 1;
		pq_bubbledown(q, 1);
	}
	return min;
}

void pq_bubbledown(priority_queue *q, int n){
	int i, c, min_index;
	min_index = n;
	c = pq_lchild(n);

	for(i=0; i<=1; i++){
		if ((c+i)<=q->n){
			if (q->q[c+i] < q->q[min_index]) min_index = c+i;
		}
	}

	if (min_index != n){
		pq_swap(q, n, min_index);
		pq_bubbledown(q, min_index);
	}

}

void heapsort(int arr[], int n){
	int i;
	priority_queue q;
	make_heap(&q, arr, n);
	for (i=0; i<n; i++)
		arr[i] = extract_min(&q);
}typedef struct queue
{
	int q[PQ_SIZE+1]; 		/* PQ Array */
	int n;					/* PQ counter */
} priority_queue;