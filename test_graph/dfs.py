from graph import *
import numpy as np
import pprint
from collections import OrderedDict


class DFS(object):
	def __init__(self, graph):

		if not isinstance(graph, Graph):
			raise TypeError("Must be of type Graph")

		self.graph = graph
		self.n     = graph.n

		self.discovered = np.array(\
			[False for i in range(self.n)]\
		)
		self.processed  = np.array(\
			[False for i in range(self.n)]\
		)
		self.parents = np.full((self.n, ), -1)

		self.entry = np.zeros((self.n, ), dtype=int)
		self.exit  = np.zeros((self.n, ), dtype=int)
		self.time  = 0

	def process_vertex_early(self, x):
		pass

	def process_vertex_late(self, x):
		pass

	def process_edge(self, x, y):
		pass

	def dfs(self, x):
		self.discovered[x]    = True
		self.process_vertex_early(x)
		self.entry[x]         = self.time
		self.time 			 += 1

		for y in self.graph.get_neighbors(x):
			self.process_edge(x, y)
			if not self.discovered[y]:
				self.parents[y] = x
				self.dfs(y)
		self.processed[x] = True
		self.process_vertex_late(x)
		self.exit[x]         = self.time
		self.time 			+= 1

	def get_state_info(self):
		state = []
		for n in range(self.n):
			state_n      		  = {} # OrderedDict()
			state_n["node"]       = n
			state_n["discovered"] = self.discovered[n]
			state_n["processed"]  = self.processed[n]
			state_n["parent"]     = self.parents[n]
			state_n["entry"]      = self.entry[n]
			state_n["exit"]       = self.exit[n]

			state.append(state_n)
		return state


if __name__ == '__main__':
	graph = Graph(5)
	graph.add_edges(1, [2, 3, 4])
	graph.add_edges(2, [4, 3])
	graph.add_edges(3, [4, 0])
	graph.print_graph()
	dfs = DFS(graph)
	dfs.dfs(1)

	pprint.pprint(dfs.get_state_info())

