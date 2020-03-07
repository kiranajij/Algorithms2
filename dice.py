def run(sv, k, n):
    # print(sv, k, n)
    if k == n:
        process(sv, k, n)
        return

    for cand in generate_cands(sv, k, n):
        sv[k] = cand
        run(sv, k+1, n)

def process(sv, k, n):
    global s
    if sum(sv)==s:
        print(sv)
        global counter
        counter += 1

def generate_cands(sv, k, n):
    global s
    cs = sum(sv[:k])
    required = s - cs

    cands = [i for i in range(1, 7) if i <= required]
    return cands

counter = 0
n = int(input("Enter number of dices:\t"))
s = int(input("Enter the required sum:\t"))
sv = [0 for i in range(n)]

# sv = []
# for i in range(n):
#     sv.append(None)

run(sv, 0, n)
print("Total = ", counter)
