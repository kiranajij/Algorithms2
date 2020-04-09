from collections import defaultdict
from itertools import chain


def case():
    N, M = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    lcm_dict = defaultdict(int)
    for n in nums:
        factors = factorize(n)
        # print(n, factors)
        for f, c in factors:
            old_power = lcm_dict.get(f, 0)
            if c > old_power:
                lcm_dict[f] = c

    max_lcm = 1
    desired = 0

    for i in range(1, M+1):
        factors = factorize(i)
        dict_copy = lcm_dict.copy()
        for f, c in factors:
            old_power = dict_copy.get(f, 0)
            if c > old_power:
                dict_copy[f] = c

        lcm = 1
        # print(dict_copy)
        for f in dict_copy:
            c = dict_copy[f]
            lcm *= f**c
        if lcm > max_lcm:
            max_lcm = lcm
            desired = i

    print(desired)


def factorize(n):
    factors = []
    i = 2
    count = 0
    while i<=n:
        count = 0
        while n%i == 0:
            count += 1
            n = n//i

        if count != 0:
            factors.append((i, count))

        i += 1
    return factors

def main():
    tc = int(input())
    for i in range(tc):
        case()

main()
