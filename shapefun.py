import turtle

"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

x = -100
y = -200
r = 100
def draw_jackolantern(t, x, y, r):
    draw_pumpkin(t, x, y, r)
    size = 2/5*r
    draw_eye(t, x+r//3 + size // 2 -r*0.15, y+r*1.2, size)
    draw_eye(t, x-r//3 - size // 2 - r*0.15, y+r*1.2, size)
    draw_mouth(t, x-r//2, y+r//2, r*1.1)


# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkred")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t: turtle.Turtle, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    base = radius // 5
    side = radius // 2
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(x + base // 2, y + 2 * radius)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

import random

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

draw_jackolantern(t, x, y, r)
draw_jackolantern(t, x+250, y, r*1.3)
draw_jackolantern(t, x-100, y+200, r*0.4)

draw_sky(t, 15)


# Example usage
#draw_polygon(t, 6, 50)  # Hexagon

# Example usage
#draw_circle(t, 50)

# Example usage
#draw_square(t, 100)

# Close the turtle graphics window when clicked
turtle.exitonclick()