def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    a = factorial(n)  # a = n!
    b = factorial(n - k)  # b = (n - k)!
    c = factorial(k)  # c = k!

    return int(a / (b * c))  # n! / ((n - k)! · k!)
    # return int(factorial(n) / (factorial(n - k) * factorial(k)))  # n! / ((n - k)! · k!)


