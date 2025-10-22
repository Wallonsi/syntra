from functools import partial
import turtle

def polygon(size: int, sides: int):
    """
    This function created a polygon with side length of size and length of sides using Turtle.

    :param size: int: the length of the sides
    :param sides: int: the number of sides
    :return: None
    """
    bob = turtle.Turtle()

    for i in range(sides):
        bob.forward(size)
        bob.left(360/sides)

    turtle.mainloop()

square = partial(polygon, sides=4)
pentagon = partial(polygon, sides=5)

def main():
    #polygon(100, 4)
    #square(100)
    pentagon(100)

if __name__ == '__main__':
    main()
