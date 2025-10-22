def factorial(n):
    assert n >= 0, "n must be greater than or equal to 0"

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))



