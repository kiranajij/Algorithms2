def staircase(height: int, step_size: list):
    if height < 0:
        return 0
    ways = 0
    for i in step_size:
        if height == i:
            ways += 1
        else:
            ways += staircase(height - i, step_size)
    return ways
    # ways = 1
    # for i in step_size:
    #     ways += staircase(height-i, step_size)
    # return ways


def implementation_2(height: int,
                     step_sizes: list,
                     cache: dict = None) -> int:
    """
    :raises: No exception.
    :rtype: integer denoting number of ways.
    :param height: height of the staircase
    :param step_sizes: Allowed step sizes, step_sizes is required to be sorted.
    :return: return the number of ways to reach to the top
            with the available step sizes.
    :example:
        Q. How many ways there are to reach to the top of a staircase of height
            5 with allowed step sizes {1, 2}
        Ans.
            >>> implementation_2(5, [1, 2])
            >>> 8
        thus number of ways is 8.


    """
    if cache is None:
        cache = {}
    ways = 0
    if height == 0:
        return 1
    elif height == step_sizes[0]:
        return 1
    else:
        for size in step_sizes:
            if height >= size:
                if not height - size in cache:
                    cache[height - size] = implementation_2(height - size,
                                                            step_sizes,
                                                            cache)
                ways += cache[height - size]
        return ways


if __name__ == '__main__':
    param = [10, [1, 2]]
    # print(staircase(*param))
    print(implementation_2(*param))
