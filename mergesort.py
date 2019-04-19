def merge(l, top, middle, end):
    i = top
    buffer1 = l[top:middle]
    buffer2 = l[middle:end]

    while not (len(buffer1) == 0 or len(buffer2) == 0):
        if buffer1[0] >= buffer2[0]:
            l[i] = buffer1.pop(0)
        else:
            l[i] = buffer2.pop(0)
        i += 1
    while len(buffer1) != 0:
        l[i] = buffer1.pop(0)
        i += 1
    while len(buffer2) != 0:
        l[i] = buffer2.pop(0)
        i += 1


def mergesort(l, top, bott):
    if top < bott-1:
        middle = (top + bott) // 2
        mergesort(l, top, middle)
        mergesort(l, middle, bott)
        merge(l, top, middle, bott)


def main():
    # l = [1, 22, 54, 12, 43, 21, 54, 23, 123, 43, 65, 23, 44, 66, 33, 67, 43, 76, 90, 12]
    l2 = [1, 3, 2, 5, 3, 6]
    mergesort(l2, 0, 5)
    print(l2)


main()
