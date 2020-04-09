def round():
    n = int(input())
    team_g = list(scan_input())
    opponent = list(scan_input())

    team_g.sort()
    opponent.sort()

    i = 0; j=0
    count = 0
    while i < n and j < n:
        if team_g[i] > opponent[j]:
            count += 1
            i += 1
            j += 1
        else:
            i+= 1
    print(count)

def scan_input():
    l = map(lambda x: int(x), input().split())
    return l

def main():
    tc = int(input())
    for i in range(tc):
        round()

main()