#!/usr/bin/env python3
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

def random_walk(n, x_start=0, y_start=0, p=np.repeat(0.25, 4)):
    ''' Simulate a two-dimensional random walk.

    Args:
        n           number of steps
        x_start     starting x position
        y_start     starting y position
        p           probabilities of (right, left, up, down)

    Returns:
        Two Numpy arrays containing the x and y coordinates, respectively, at
        each step (including the initial position).
    '''
    # Sample the steps.
    steps = np.random.choice(4, size=n, p=p)

    # Preallocate position vectors.
    x_steps = np.zeros(n + 1, dtype='int')
    y_steps = np.zeros(n + 1, dtype='int')

    # Fill in the steps.
    x_steps[0], y_steps[0] = x_start, y_start

    x_steps[1:] += (steps == 0)
    x_steps[1:] -= (steps == 1)

    y_steps[1:] += (steps == 2)
    y_steps[1:] -= (steps == 3)

    # Compute the positions.
    x = x_steps.cumsum()
    y = y_steps.cumsum()

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

