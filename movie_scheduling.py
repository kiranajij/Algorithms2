def schedule(schedules):
    lst = schedules[::]
    res = []
    while len(lst):
        task = min(lst, key=lambda x: x[1])
        res.append(task)
        lst.remove(task)
        for i, item in enumerate(lst):
            if item[1] > task[0] or item[0] < task[1]:
                lst.remove(item)
    return res


print(schedule([[0, 2],
                [1, 4],
                [1, 3],
                [3, 4]]))
