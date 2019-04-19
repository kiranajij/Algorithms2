#define MAXVERT 1000
#include <stdio.h>

typedef struct edgenode {
	int y;		// adjacency Info
	int weight;			// edge weight if any
	struct edgenode *next;		//Next node on list
} edgenode;

typedef struct {
	edgenode *edges[MAXVERT+1]; 		//adjacency info
	int degree[MAXVERT+1];				//outdegree of each vertex
	int nvertices;						//number of vertices
	int nedges;							//number of edges
	bool directed;						//for directed graphs
} graph;

void initialize_graph(graph *g, bool directed){
	int i;

	g->nvertices = 0;
	g-> nedges = 0;
	g->directed = directed;

	for (i=1; i<=MAXVERT; i++){
		g->degree[i] = 0;
		g->edges[i] = NULL;
	}
}

void read_graph(graph *g, bool directed){
	int i, n, x, y;

	initialize_graph(g, directed);
	scanf("%d %d", &(g->nvertices), &n);

	for (i=0; i<n; i++){
		scanf("%d %d", &x, &y);
		insert_edge(g, x, y, directed);
	}
}