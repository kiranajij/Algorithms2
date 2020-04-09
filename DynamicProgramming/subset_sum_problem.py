"""
Given a set of non-negative integers, and a value sum, determine if there is a 
subset of the given set with sum equal to given sum.

Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""
possible = False

def subset_sum(st, value, k):
    # Suppose we are working witht he k'th element, so either
    # the subset contains element or it doesn't

    # we find it recursively, 

    # The boundary conditions
    global possible
    if possible:
        return
    if value == 0:
        possible = True
        return
    if value < 0 or k == len(st):
        return

    subset_sum(st, value-st[k], k+1)
    subset_sum(st, value, k+1)

if __name__ == '__main__':
    s = [3, 34, 12, 5, 2]
    val = 5
    subset_sum(s, val, 0)
    print(possible)

