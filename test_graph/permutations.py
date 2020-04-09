array = [1, 2, 3, 4]
l = len(array)
sv  = [None for i in range(l)]

def perms(arr, arr_len, n, sv):
    if n == arr_len:
        print("".join(map(lambda x: str(x), sv)))
        return
    possible_elem = [e for e in arr if e not in sv[0:n]]
    # print(possible_elem)
    for elem in possible_elem:
        sv[n] = elem
        perms(arr, arr_len, n+1, sv)

sv_subsets = [None for i in range(l)]
def subsets(arr, arr_len, n, sv_subsets):
    if n == arr_len:
        subset = [arr[i] for i in range(arr_len) if sv_subsets[i]]
        print("".join(map(lambda x: str(x), subset)))
        return

    possible_elem = [False, True]
    for e in possible_elem:
        sv_subsets[n] = e
        subsets(arr, arr_len, n+1, sv_subsets)

if __name__ == '__main__':
    perms(array, l, 0, sv)
    print('-'*50)
    subsets(array, l, 0, sv_subsets)