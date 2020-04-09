from collections import defaultdict

def case():
    text = input()
    k, x = list(map(int, input().split()))

    counts = defaultdict(int)

    # Count the occuraces of each character
    for c in text:
        counts[c] += 1

    # good pref count
    good_pref_count = 0
    exceed = []

    # count how many exceeds
    for c, count in counts.items():
        if count > x:
            exceed.append(count-x)
        else:
            good_pref_count += 1

    exceed.sort()
    for i in exceed:
        if i <=k:
            good_pref_count += 1
            k -= i
        else:
            break
    print(good_pref_count)

def main():
    tc = int(input())
    for i in range(tc):
        case()

main()