"""
>>>

"""

def swap(lst, i1, i2):
    lst[i1], lst[i2] = lst[i2], lst[i1]


def partition(lst, start, end):
    tc = start
    p_i = end
    pivot = lst[end]
    for i in range(start, end):
        if lst[i] < pivot:
            swap(lst, tc, i)
            tc += 1
    swap(lst, tc, p_i)
    # print(lst)
    return tc


def quicksort(lst, start, end):
    if end > start:
        mid = partition(lst, start, end)
        quicksort(lst, start, mid-1)
        quicksort(lst, mid+1, end)