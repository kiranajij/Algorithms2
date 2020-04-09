import numpy as np

def lcs_naive(s1, s2, i, j):
    global mask1, mask2
    if i == -1 or j == -1:
        return 0
    if s1[i] == s2[j]:
        return 1+lcs_naive(s1, s2, i-1, j-1)
        mask1[i] = mask2[j] = True
    else: 
        m1 = lcs_naive(s1, s2, i-1, j)
        m2 = lcs_naive(s1, s2, i, j-1)

        if m1 > m2:
            mask1[i] = True
            return m1
        else:
            mask2[j] = True
            return m2

def lcs_dynamic(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp = np.zeros((n1, n2), dtype=int)

    for i in range(n1):
        dp[i, 0] = 1 if s1[i] == s2[0] else 0
    for i in range(n2):
        dp[0, i] = 1 if s1[0] == s2[i] else 0

    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i] == s2[j]:
                dp[i, j] = 1+dp[i-1, j-1]
            else:
                dp[i, j] = max(
                    dp[i-1, j],
                    dp[i, j-1]
                )
    return dp[n1-1, n2-1]


if __name__ == '__main__':
    while True:
        i1 = input()
        i2 = input()
        m = lcs_dynamic(i1, i2)
        print(m)
