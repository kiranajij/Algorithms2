"""
Given an sorted array and an integer x, find the first and last occurance of x.
"""

arr     =   [2, 3, 6, 7, 8, 8, 8, 8, 10, 10, 10]
x       =   8


# Find the first and last index of `x` in `arr`
def first_occurance(arr, x, low, high):
    first_occur = -1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            first_occur = mid
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1

    return first_occur


if __name__ == '__main__':
    fo = first_occurance(arr, x, 0, len(arr)-1)
    print(fo)
    print(list(enumerate(arr)))