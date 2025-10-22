# import turtle
#
# def draw_triangle(points, color, t):
#     t.fillcolor(color)
#     t.up()
#     t.goto(points[0])
#     t.down()
#     t.begin_fill()
#     t.goto(points[1])
#     t.goto(points[2])
#     t.goto(points[0])
#     t.end_fill()
#
# def midpoint(p1, p2):
#     return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
#
# def sierpinski(points, depth, t):
#     colors = ['purple']
#     draw_triangle(points, colors[depth % len(colors)], t)
#
#     if depth > 0:
#         sierpinski([points[0],
#                     midpoint(points[0], points[1]),
#                     midpoint(points[0], points[2])],
#                    depth - 1, t)
#         sierpinski([points[1],
#                     midpoint(points[0], points[1]),
#                     midpoint(points[1], points[2])],
#                    depth - 1, t)
#         sierpinski([points[2],
#                     midpoint(points[2], points[1]),
#                     midpoint(points[0], points[2])],
#                    depth - 1, t)
#
# # --- main ---
# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
#
# points = [[-150, -100], [0, 150], [150, -100]]
# sierpinski(points, 4, t)
#
# turtle.done()


# import turtle
#
# def koch(t, x):
#     if x < 5:
#         t.forward(x)
#     else:
#         koch(t, x / 3)
#         t.left(60)
#         koch(t, x / 3)
#         t.right(120)
#         koch(t, x / 3)
#         t.left(60)
#         koch(t, x / 3)
#
# # --- main ---
# t = turtle.Turtle()
# t.color("purple")
#
# koch(t, 120)
#
# turtle.done()

# from jupyturtle import forward, left, right, back
#
# def draw(length):
#     angle = 50
#     factor = 0.6
#
#     if length > 5:
#         forward(length)
#         left(angle)
#         draw(factor * length)
#         right(2 * angle)
#         draw(factor * length)
#         left(angle)
#         back(length)


import turtle

def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        turtle.forward(length)
        turtle.left(angle)
        draw(factor * length)
        turtle.right(2 * angle)
        draw(factor * length)
        turtle.left(angle)
        turtle.backward(length)

turtle.color("purple")
turtle.speed(0)

draw(100)
turtle.done()

