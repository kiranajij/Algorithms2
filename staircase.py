def staircase(height: int,
              step_sizes: list,
              cache: dict = None) -> int:
    """
    :param cache: cache stores a cache of each visit. If cache is not provided
                during the call the a blank $dict$ is initialized. Then this
                instance is updated and reused in the recursive calls.
    :raises: No exception.
    :rtype: integer denoting number of ways.
    :param height: height of the staircase
    :param step_sizes: Allowed step sizes, step_sizes is required to be sorted.
    :return: return the number of ways to reach to the top
            with the available step sizes.
    =============================================================================
    :example:
        Q. How many ways there are to reach to the top of a staircase of height
            5 with allowed step sizes {1, 2}
        Ans.
            >>> staircase(5, [1, 2])
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
                    cache[height - size] = staircase(height - size,
                                                     step_sizes,
                                                     cache)
                ways += cache[height - size]
        return ways


if __name__ == '__main__':
    param = [10, [1, 2]]
    # print(staircase(*param))
    print(staircase(*param))
