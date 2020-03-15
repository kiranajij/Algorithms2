def cost_match_string(str1: str, str2: str, i :int, j: int):
    lowest_cost = None

    if i==0: return j+1
    if j==0: return i+1

    costs = [None for i in range(3)]

    if (str1[i] == str2[j]):
        costs[0] = cost_match_string(str1, str2, i-1, j-1)
    else:
        costs[0] = cost_match_string(str1, str2, i-1, j-1) + 1
    
    costs[1] = cost_match_string(str1, str2, i, j-1) + 1
    costs[2] = cost_match_string(str1, str2, i-1, j) + 1

    lowest_cost = min(costs)

    return lowest_cost

if __name__ == "__main__":
    while True:
        s = input()
        pat = input()

        len_s = len(s) - 1
        len_pat = len(pat) - 1

        cost = cost_match_string(s, pat, len_s, len_pat)
        print(f"Cost is {cost}")