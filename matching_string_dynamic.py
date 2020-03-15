import numpy as np


class cell:

    MATCH  = 0
    INSERT = 1
    DELETE = 2

    def __init__(self, cost=None, parent=None):
        self.cost = cost
        self.parent = parent
    
    def __repr__(self):
        # return f"({self.parent}, {self.cost})"
        dig = None
        if self.parent == None: dig='0'
        else: dig = list(['M', 'I', 'D']).__getitem__(self.parent)

        return f"{dig}{self.cost:02d}"

def match_string_dynamic(str1, str2, ci, cj):
    # Initialize the array to store the elements
    m = np.array([ [cell() for i in range(cj+1)] for j in range(ci+1)])
    
    for i in range(ci+1):
        m[i, 0].cost = i
    for j in range(cj+1):
        m[0, j].cost = j
    
    for i in range(ci):
        for j in range(cj):
            mi = i+1
            mj = j+1

            costs = [cell() for i in range(3)]
            if str1[i] == str2[j]:
                costs[0].cost = m[mi-1, mj-1].cost
                costs[0].parent = cell.MATCH
            else:
                costs[0].cost = m[mi-1, mj-1].cost + 1
                costs[0].parent = cell.MATCH
            
            costs[1].cost = m[mi-1, mj].cost + 1
            costs[1].parent = cell.DELETE

            costs[2].cost = m[mi, mj-1].cost + 1
            costs[2].parent = cell.INSERT

            min_cell = min(costs, key=lambda x: x.cost)
            m[mi, mj] = min_cell
    
    path = reconstruct(m, ci, cj)
    

def reconstruct(m, ci, cj):
    pass

s = "Fucker"
pat = "Sucker"

slen, plen = len(s), len(pat)
match_string_dynamic(pat, s, slen, plen)
