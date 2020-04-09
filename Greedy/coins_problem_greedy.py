"""
Skiena problem 8-6
"""

def select_coins_greedy(coins: list, target: int):
    coins.sort(reverse=True)   # Sort them in descending order

    required = []

    for val in coins:
        while val <= target:
            required.append(val)
            target -= val

    if target != 0:
        return None
    else:
        return required


if __name__ == '__main__':
    coins = [1, 6, 10]
    while True:
        target = int(input())
        req = select_coins_greedy(coins, target)
        print(req)

