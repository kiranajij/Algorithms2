def case():
    a, b = input().split()
    la = len(a)
    lb = len(b)

    max_sum = int(a)+int(b)
    # print(a, b)
    for i in range(la):
        for j in range(lb):
            lst_a = list(a)
            lst_b = list(b)
            lst_a[i], lst_b[j] = lst_b[j], lst_a[i]

            new_a = int("".join(lst_a))
            new_b = int("".join(lst_b))
            # print(new_a, new_b)
            s = new_a + new_b
            if s > max_sum:
                # print("s=", s)
                max_sum = s
    print(max_sum)


def main():
    tc = int(input())
    for i in range(tc):
        case()

main()

