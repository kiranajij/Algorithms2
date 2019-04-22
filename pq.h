# ifndef HEADER_PQ
# define HEADER_PQ

# define PQ_SIZE 30

typedef struct queue
{
	int q[PQ_SIZE+1]; 		/* PQ Array */
	int n;					/* PQ counter */
} priority_queue;
int pq_parent(int);
int pq_lchild(int);
void pq_bubbleup(priority_queue*, int);
void pq_insert(priority_queue*, int);
void pq_init(priority_queue*);
void make_heap(priority_queue*, int[] , int);
void pq_swap(priority_queue*, int, int);
void pq_bubbledown(priority_queue*, int); 
void heapsort(int[], int);

# endif