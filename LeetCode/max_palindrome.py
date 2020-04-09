# Method-1

def expand_palindrome(s, L, R):
    """"
    0 1 2 3 4 5 6 7 8 9 10 11   : Positions
      0   1   2   3   4     5   : Indices
    * a * b * a * a * b  *  a   : String
              ^-> L= 2, R = 2
                ^-> L=2, R=3

    returning the total lenght length of the palindrome
    expanded from the centre L,R.

    """

    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1

    return (R-L-1)

def max_palindrome(s):
    start = 0
    end   = 0

    max_so_far = 0

    for i in range(len(s)):
        l1 = expand_palindrome(s, i, i)
        l2 = expand_palindrome(s, i, i+1)
        print(i, l1, l2)

        l_max = max(l1, l2)
        if l_max > max_so_far:

            max_so_far = l_max
            start = i - (l_max-1)//2
            end   = i + l_max//2

    return s[start:end+1]


while True:
    s = input()
    print(max_palindrome(s))
