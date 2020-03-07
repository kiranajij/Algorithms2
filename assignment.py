import numpy as np

""" This is the scanning part"""
n = int(input())  # order of the payoff matrix
costs = np.zeros((n, n))

for i in range(n):
    line = str(input())  # rows of the payoff matrix
    line_split = list(line.split(" "))
    costs[i] = np.asarray(list(map(lambda x: float(x), line_split)))

n = 5
sv = np.zeros((n, 1))  # state vector of the system


def candidates(sv, k):
    cands = []
    for i in range(n):  # i: an element of the sv
        if i not in sv:
            cands.append(i)

    return cands


MIN_COST = np.inf
MIN_SV = None


def search(sv, k):
    global MIN_COST, MIN_SV
    if k == n:
        cost = 0
        for i in range(n):
            j = sv[i]
            cost += costs[i][j]
        if cost < MIN_COST:
            MIN_COST = cost
            MIN_SV = sv.copy()

    # check cost
    else:
        cands = candidates(sv, k)
        for i in cands:
            sv.append(i)
            search(sv, k + 1)
            sv.pop(-1)


if __name__ == '__main__':
    # print(candidates([1, 2, 3], 3))
    search([], 0)
