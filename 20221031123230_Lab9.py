"""
a)
>>> forward(900)
Traceback (most recent call last):
NameError: name 'forward' is not defined
An error occurs when I type foward(900) without importing turtle
b)
>>> from turtle import *
>>> forward(100)
A pop up appears and draws a line towards the rigth
d)
>>> circle(100)
It drew a circle
"""
from turtle import *
from math import sin, cos, gcd, pi

def draw_polygon(n_sides, x, y, length, color):
    """Draws a polygon."""
    if n_sides<3 or (type(n_sides) != int):
        d = 'Invalid input for number of sides'
        return d
    if (type(x) != int):
        f = 'Invalid Coordinates'
        return f
    if (type(length) != int) or length<0:
        t = 'Invalid length'
        return t
    speed(5)
    penup()
    goto(x,y)
    pendown()
    pencolor(color)
    for i in range(n_sides):
        forward(length)
        left(360/n_sides)

# draw_polygon(3, 0, 0, 100, 'orange')
# draw_polygon(5, 200, -200, 100, 'red')
# draw_polygon(8, -200, -100, 100, 'blue')

def iterative_spiral(n):
    """Draws a spiral using while loop"""
    x = n
    y=1
    while x>0:
        circle(x,30)
        x -= 2
def recursive_spiral(n):
    x = n
    circle(x,30)
    if x>0:
        recursive_spiral(x-2)
# speed(0)
# penup()
# goto(100,200)
# pendown()
# iterative_spiral(120)
# penup()
# goto(200,200)
# pendown()
# recursive_spiral(120)

def draw_tree(trunk_length, levels):
    """Draws a tree"""
    if levels>= 0:
        width(levels+3)
        forward(trunk_length)
        left(30)
        draw_tree(trunk_length-10, levels-1)
        right(30)
        right(30)
        draw_tree(trunk_length-10, levels-1)
        left(30)
        backward(trunk_length)

# speed(0)
# penup()
# goto(0,-300)
# pendown()
# left(90)
# draw_tree(100,8)

def hypotrochoid(a, b, h, color):
    speed(0)
    width(2)
    pencolor(color)
    d = 0.04
    max1 = 2*(pi)*((LCM(a,b))/a)
    r = 0
    penup()
    goto(((a-b)+h),0)
    pendown()
    while r <= max1:
        z = ((a-b)/b)*r
        x = (a-b) * cos(r) +h* cos(z)
        y = (a-b) * sin(r) -h* sin(z)
        goto(x,y)
        r=r+d
        
def LCM(x,y):
    f = ((abs(x*y))/(gcd(x,y)))
    return f


# hypotrochoid(300, 180, 75, 'orange')
# hypotrochoid(125, 75, 125, 'red')
# hypotrochoid(200, 40, 60, 'yellow')