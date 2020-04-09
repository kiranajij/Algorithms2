def case():
    n = int(input())
    names = input().split()
    initials = ""
    counts = {}
    for name in names:
        c = name[0]
        initials += c
        counts[c] = get(c, 0) + 1
    print (initials)
    for k, val in counts.items():
        if val == 1:
            print (f"I am Alone {k}")

def main():
    tc = int(input())
    for i in range(tc):
        case()

main()