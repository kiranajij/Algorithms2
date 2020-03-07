"""
>>> max_sum([-1, 8, 4])[1]
12
>>> test([-1, 7, 8, -5, 4])
48
>>> test([3, 2, 1, -1])
13
>>> test([11, 12, -2, -1])
12
>>> test([4, 5, 4, 3 ])
44
>>> test([5, 10, 4, -1])
10
"""


def max_sum(lst):
    n = len(lst)
    ordr = [i for i in range(n)]
    ordr.sort(key=lambda i: lst[i], reverse=True)
    res = []
    s = 0
    for i in ordr:
        if lst[i] < 0:
            break
        res.append(i)
        s += lst[i]
    return res, s


def comp_lst(lst1, lst2):
    n = min(len(lst1), len(lst2))
    for i in range(n-1, 0, -1):
        if lst1[i] < lst2[i]:
            # print(lst2)
            return 2

        elif lst1[i] > lst2[i]:
            # print(lst1)
            return 1



def test(lst):
    lst1 = lst[0::2]
    lst2 = lst[1::2]

    r1, s1 = max_sum(lst1)
    r2, s2= max_sum(lst2)

    if s1<s2:
        r2.sort(reverse=True)
        for i in r2:
            print(f"{lst2[i]}", end="")
    elif s2<s1:
        r1.sort(reverse=True)
        for i in r1:
            print(f"{lst1[i]}", end="")
    elif s1 == s2:
        if comp_lst(lst1, lst2) == 1:
            s = s1; lst = lst1; r=r1
        else:
            s = s2; lst = lst2; r=r2
        lst.sort(reverse=True)
        for i in r:
            print(f"{lst[i]}", end="")


# tc = int(input())

test([4, 5, 4, 3 ])