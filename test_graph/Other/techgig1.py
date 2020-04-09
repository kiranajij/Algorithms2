def main():
    n = int(input())

    req = list(scan_input())
    have = list(scan_input())

    # print(n)
    # print(req)
    # print(have)

    max_amt = have[0] // req[0]
    for r, h  in zip(req, have):
        a = h // r
        # print(a, max_amt)
        if a < max_amt:
            max_amt = a
    print(max_amt)

def scan_input():
    l = map(lambda x: int(x), input().split())
    return l

main()