import turtle

# def rectangle():
#     for i in range(2):
#         turtle.forward(80)
#         turtle.left(90)
#         turtle.forward(40)
#         turtle.left(90)
#
# def main():
#     rectangle()
#
# if __name__ == '__main__':
#     main()
#
#
# def rhombus(side_length, angle):
#     reverse_angle = 180 - angle
#
#     for _ in range(2):
#         turtle.forward(side_length)
#         turtle.left(angle)
#         turtle.forward(side_length)
#         turtle.left(reverse_angle)
#
# def main():
#     rhombus(50, 60)
#
# if __name__ == '__main__':
#     main()

def triangle(side_length, angle=60):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(180 - angle)

def main():
    triangle(100, 60)

if __name__ == '__main__':
    main()

# def triangle(length, angle=60):
#     for i in range(3):
#         turtle.forward(length)
#         turtle.left(180 - angle)
#
# def main():
#     num_triangles = 5
#     length = 100
#     interior_angle = 60
#
#     for i in range(num_triangles):
#         triangle(length, interior_angle)
#         turtle.right(360 / num_triangles)
#
# if __name__ == '__main__':
#     main()









