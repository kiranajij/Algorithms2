from collections import deque
import logging

logging.basicConfig(level=logging.DEBUG)

def solution(s):
    dq = deque()
    cache = {0: s.index('(')}
    ans = 0

    logging.debug(f"{list(enumerate(s))}")

    for i, c in enumerate(s):
        if c == ')' and len(dq) > 0:
            # When closing the parent and stack is not empty
            logging.debug(f"c is (, and len>0")
            dq.pop()

            new_len = len(dq)
            logging.debug(f"len of dq is {new_len}")

            prev = cache.get(new_len, -1)
            logging.debug(f"prev = {prev}")
            if prev > -2:
                clen = i-prev+1
                ans = max(clen, ans)
                logging.debug(f"clen = {clen}, ans = {ans}")
            else:
                cache[new_len] = i
                logging.debug(f"adding {prev} to cache")
        elif c == '(':
            # When opening the parenthesis.
            logging.debug(f"c=(, pushing to dq")
            dq.append(i)
            logging.debug(f"dq = {dq}")
        else:
            # When closing the paren and the stack is empty
            # dq.clear()
            cache = {0: i+1 }
            logging.debug(f"Clearing deque, index {i}, cache[0] = {i+1}")

    return ans


if __name__ == '__main__':
    while True:
        s = input()
        ans = solution(s)
        print(ans)