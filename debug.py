def main():
    var1 = 2 #rename alle variables: rechtsklik op de variable en rename
    var2 = 5

    assert var1 + var2 == 7  # ga er van uit dat a + b = 7 <- assert betekenis
    assert som(var1, var2) == 7

def som(a, b):
    c = a + b - 1

    return c

if __name__ == '__main__':
    main()
