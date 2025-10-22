import math

def factorial(n):
    # if n == 0 or n == 1:
    #     return 1
    #
    # return n * factorial(n - 1)
    if n == 0:
        return 1

    result = n

    for i in range(2, n):
        result *= i

    return result

def main():
    assert factorial(1) == 1, "factorial(1) must be 1"
    assert factorial(3) == 6, "factorial(3) must be 6"
    assert factorial(4) == 24, "factorial(5) must be 24"

    x = factorial(7)
    print("De faculteit van x is", x)

if __name__ == '__main__':
    main()