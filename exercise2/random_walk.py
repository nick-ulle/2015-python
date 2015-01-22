'''
A two-dimensional random walk simulator and animator.
'''

# The turtle package is part of Python's standard library. It provides some
# very primitive graphics capabilities. For more details see
#
#   https://docs.python.org/3/library/turtle.html
#
import turtle

import numpy as np

def random_walk(n):
    ''' Simulate a two-dimensional random walk.

    Args:
        n           number of steps

    Returns:
        Two Numpy arrays containing the x and y coordinates, respectively, at
        each step (including the initial position).
    '''

    # Your task: fill this in.

    return x, y



# Notice that the documentation automatically shows up when you use ?
def draw_walk(x, y, speed = 'slowest', scale = 20):
    ''' Animate a two-dimensional random walk.

    Args:
        x       x positions
        y       y positions
        speed   speed of the animation
        scale   scale of the drawing
    '''
    # Reset the turtle.
    turtle.reset()
    turtle.speed(speed)

    # Combine the x and y coordinates.
    walk = zip(x * scale, y * scale)
    start = next(walk)

    # Move the turtle to the starting point.
    turtle.penup()
    turtle.goto(*start)

    # Draw the random walk.
    turtle.pendown()
    for _x, _y in walk:
        turtle.goto(_x, _y)

