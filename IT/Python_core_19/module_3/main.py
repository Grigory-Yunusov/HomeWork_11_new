def fib(n):
    if n == 0:
        return 0

    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def iterative_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(iterative_fib(8))