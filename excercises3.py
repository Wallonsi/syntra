def print_right(text):
    spaces = 40 - len(text)
    print(' ' * spaces + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")




def triangle(symbol, height):
    for i in range(1, height + 1):
        print(symbol * i)

triangle('L', 5)

