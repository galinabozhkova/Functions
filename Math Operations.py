from collections import deque


def math_operations(*args, **kwargs):
    new_queue = deque(args)

    while len(new_queue) >= 4:
        kwargs["a"] += new_queue.popleft()
        kwargs["s"] -= new_queue.popleft()
        if new_queue[0]!=0:
            kwargs["d"] /= new_queue.popleft()
        else:
            new_queue.popleft()
        kwargs["m"] *= new_queue.popleft()

    if len(new_queue)>=1:
        kwargs["a"] += new_queue.popleft()
    if len(new_queue) >= 1:
        kwargs["s"] -= new_queue.popleft()
    if len(new_queue) >= 1 and new_queue[0]!=0:
            kwargs["d"] /= new_queue.popleft()

    kwargs = sorted(kwargs.items())
    kwargs = sorted(kwargs, key = lambda x: x[1], reverse=True)
    result = ''
    for el in kwargs:
        result += f"{el[0]}: {el[1]:.1f}"+"\n"

    return result




print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
