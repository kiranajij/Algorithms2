"""
# The partition Problem
---

Problem : Integer partition without rearrangement
Input   : An arrangement S of nonnegative numbers {s1, s2, ..., sn} 
    and an integer k.
Output  : Partition S into k or fewer ranges, to minimize the maximum sum over
    all the ranges.

So called `Linear Partitioning Problem`(Without rearrangement)
"""
import numpy as np
import itertools

class Partition:
    def __init__(self, s, k):
        self.s = [None] + s
        self.k = k
        self.n = len(s)
        self.darray = np.full((self.n+1, self.k+1), 0)
        self.divs = np.full((self.n+1, self.k+1), 0)

    def run(self):
        dp = self.darray
        n = self.n
        s = self.s
        k = self.k
        divs = self.divs
        p = [0 for i in range(n+1)]
        for i in range(1, n+1):
            p[i] = s[i]+p[i-1]

        # The initial condition
        for i in range(1, k+1):
            dp[1, i] = s[1]
        for i in range(1, n+1):
            dp[i, 1] = p[i]

        for pk, pn in itertools.product(range(2, k+1), range(2, n+1)):
            tmp = []
            for x in range(1, pn):
                dp[pn, pk] = 100000
                cost = max(dp[x, pk-1], p[pn]-p[x])
                if dp[pn, pk] > cost:
                    dp[pn, pk] = cost
                    divs[pn, pk] = x
        return dp, divs


def partition(s, num):
    l = len(s)
    darr = np.full((l, num), 0)
    for i in range(l):
        darr[i, 0] = sum(s[:i+1])
    for j in range(num):
        darr[0, j] = s[0]

    for i in range(1, l):
        for j in range(1, num):
            temp = []
            for x in range(i-1):
                m = darr[x, j-1]
                o = sum(s[x+1:])
                t = max(m, o)
                temp.append(t)
            m = min(temp)
            darr[i, j] = m

    return darr


if __name__ == '__main__':
    s = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    k = 3
    s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k2 = 3
    dp = Partition(s1, k2)
    # d, p = dp.run()
    # print(d)
    # print(p)
    # from itertools import accumulate
    # [print(i) for i in accumulate(s)]

    d = partition([1]*9, k2)
    print(d)