"""
# The Knapsack problem
---

    Think You're a Robber and you have a limited carry capacity.
Like a bagpack which can carry only limited weight. Now imagin
coming accross a grocerry store where you can steal whatever
you want, but with a catch. Each item has a value and some weight.
You can only carry things that fit inside your bagpack. Now given
some item (value, weight) pair, find out what is the maximum amount
of value you can fit inside your knapsac.

"""

import numpy as np
import pandas as pd
from tabulate import tabulate


def knapsac(capacity, items):
    """
    Items are of the form (value, weight)
    """
    n = len(items)  # Number of items to be stored
    darray = np.zeros((n+1, capacity+1))# Dynamic array

    for i in range(1, n+1):
        for j in range(1, capacity+1):
            value, weight = items[i-1]

            darray[i, j] = darray[i-1, j]
            if weight <= j and darray[i-1, j-weight]+value > darray[i-1, j]:
                darray[i, j] = darray[i-1, j-weight] + value

    maxval = darray[n, n]
    df = pd.DataFrame(darray)
    print(tabulate(df, headers='keys', tablefmt="psql"))
    selected = []
    backtrack(darray, n, capacity, items, selected)
    return selected

def backtrack(arr, i, j, items, selected):
    if (i == 0):
        return
    if arr[i, j] == arr[i-1, j]:
        backtrack(arr, i-1, j, items, selected)
    else:
        selected.append(i)
        value, weight = items[i-1]
        backtrack(arr, i-1, j-weight, items, selected)

if __name__ == '__main__':
    capacity = 7
    objects = [
        (2, 3),
        (2, 1),
        (4, 3),
        (5, 4),
        (3, 2)
    ]
    items = pd.DataFrame(objects, columns=["value", "weight"])
    print(tabulate(items, headers='keys', tablefmt="psql"))
    selected = knapsac(capacity, objects)
    print(f"selected: {selected}")