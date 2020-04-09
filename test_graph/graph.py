from collections import OrderedDict

import numpy as np
import pandas as pd
from tabulate import tabulate


class Graph(object):
	"""
	# Graph
	---
	This is the simplest `Graph` API one can imagine.
	Contains the least number of function required for
	a graph.
	"""
	def __init__(self, n, is_directed=False):
		"""
		The initialization method of Graph takes 1 required
		argument and 1 optional argument.
		:n:	n is the number of nodes. The graph automatically
			enumerates the nodes from 0 to n-1.
		:is_directed:	If the graph is directed.
		
		It also initializes the graph data structure with an
		ordered dict and associates each node with an empty list
		as the adjacency list.

		"""
		self.n = n
		self.is_directed = is_directed
		self.graph_data = OrderedDict()
		for i in range(n):
			self.graph_data[i] = []

	def add_edge(self, i, j):
		"""
		if j is already in i's neighbor, then skip otherwise
		add to i's neghbor. Also if the graph is not directed
		,i.e. (i, j) is an edge, then so is (j ,i) so add i to
		j's adjacency list.

		"""
		adj_i = self.graph_data[i]
		adj_j = self.graph_data[j]

		if not j in adj_i:
			adj_i.append(j)
		if not self.is_directed and (not i in adj_j):
			adj_j.append(i)

	def add_edges(self, i, itr):
		"""
		Given an iterable of neighboring node of i, it adds
		all the nodes of itr to the adjacency list of i.
		"""
		for node in itr:
			self.add_edge(i, node)

	def add_edges_from_touple(self, *args):
		for x, y in args:
			if isinstance(y, int):
				self.add_edge(x, y)
			else:
				try:
					self.add_edges(x, y)
				except TypeError:
					raise ValueError("Unrecognised type")

	def get_neighbors(self, i):
		"""
		return the neighbor of i.
		More technacally, it returns an iterable over the
		adjacency list of i in the graph.
		"""
		return self.graph_data[i]

	def remove_edge(self, i, j):
		"""
		self explanatory
		"""
		adj_list_i = self.graph_data[i]
		adj_list_j = self.graph_data[j]

		try:
			adj_list_i.remove(j)
			if not self.is_directed:
				adj_list_j.remove(i)

		except ValueError:
			pass

	def print_graph(self):
		"""
		Print the graph content.
		"""
		print(self.__str__())

	def get_empty_graph(self):
		graph_copy = self.graph_data.__copy__()
		for keys in graph_copy:
			graph_copy[keys] = []
		return graph_copy


	def __iter__(self):
		"""
		Returns an iterator over all the Nodes of the graph.
		"""
		return self.graph_data.keys()

	def __copy__(self):
		"""
		Return a copy of the currenct graph.
		"""
		new_graph            = Graph(self.n)
		new_graph.graph_data = self.graph_data
		return new_graph

	def copy(self):
		return self.__copy__()

	def __str__(self):
		"""
		Returns a beautiful representation of the graph
		along with all the nodes and the neighbors.
		"""
		data = ""
		for key in self.graph_data:
			adjs = self.graph_data[key]
			data = data + "{}: {}\n".format(key, adjs) 
		return data

	def __repr__(self):
		"""
		representation of the graph.
		"""
		return "Graph<{} nodes>".format(self.n+1)


class GraphDirected(Graph):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, is_directed=True, **kwargs)


class MappedGraph(Graph):
	def __init__(self, n, items, *args, **kwargs):
		super().__init__(n, *args, **kwargs)
		self.map_name_to_id = {}	# name -> id
		self.map_id_to_name = {}	# id -> name
		for i, name in enumerate(items):
			self.map_id_to_name[i] = name
			self.map_name_to_id[name] = i

	def get_node_id(self, name):
		try:
			return self.map_name_to_id[name]
		except:
			print(f"No {name} in the graph")

	def get_node_name(self, id):
		try:
			return self.map_id_to_name[id]
		except:
			print(f"No {id} in the graph")
	def add_edge(self, x, y):
		try:
			i = self.get_node_id(x)
			j = self.get_node_id(y)

			super().add_edge(i, j)

		except KeyError:
			print(f"Warning: No {x}, {y} Node in the graph")

	def get_neighbors(self, name):
		try:
			i = self.get_node_id(name)
			neighbors = super().get_neighbors(i)

			return map(lambda x: self.get_node_name(x), neighbors)
		except KeyError:
			print(f"Warning: No {name} Node in the graph")

	def remove_edge(self, x, y):
		i = self.get_node_id(x)
		j = self.get_node_id(y)

		super().remove_edge(x, y)


	def pprint_graph(self):

		for id in self.graph_data:
			name = self.get_node_name(id)
			neighbors = list(self.get_neighbors(name))

			print(f"{name} : {neighbors}")

	def __str__(self):

		string = "\n"
		for id in self.graph_data:
			name = self.get_node_name(id)
			neighbors = list(self.get_neighbors(name))

			string += f" {name} : {neighbors} \n"
		return string

	def get_simplified_graph(self):
		graph = Graph(self.n)
		graph.graph_data = self.graph_data
		self.is_directed = self.is_directed
		return graph

	def map_ids_to_names(self, ids):
		return map(lambda x: self.get_node_name(x), ids)


class WeightedGraph(Graph):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def add_edge(self, x, y, weight):
		adj_x = self.graph_data[x]
		adj_y = self.graph_data[y]

		if not (y, weight) in self.graph_data:
			adj_x.append((y, weight))

		if not self.is_directed and (x, weight) not in self.graph_data:
			adj_y.append((x, weight))

	def add_edges(self, x, ys, weights):
		for y, weight in zip(ys, weights):
			self.add_edge(x, y, weight)

	def get_edge_weight(self, x, y):
		adj_x = self.graph_data[x]
		for node, weight in adj_x:
			if node == y:
				return weight

	def remove_edge(self, x, y):
		adj_x = self.graph_data[x]
		adj_y = self.graph_data[y]

		for i, (node, _) in enumerate(adj_x):
			if node == y:
				adj_x.pop(i)
		for j, (node, _) in enumerate(adj_y):
			if node == x:
				adj_y.pop(j)

	def __str__(self):
		new_dict = {}
		for key in self.graph_data:
			neighbors = []
			for k, w in self.graph_data[key]:
				d = f" {k}  {w} "
				neighbors.append(d)
			new_dict[key] = neighbors
		return tabulate(new_dict, "keys")
		return tabulate(self.graph_data, "keys", "simple")


if __name__ == '__main__':

	graph = WeightedGraph(4)
	graph.add_edge(0, 1, 2)
	graph.add_edges(1, [2, 3], [3, 4])
	graph.add_edge(3, 2, 5)

	print(graph)
	graph.remove_edge(1, 3)
	# print(graph)
