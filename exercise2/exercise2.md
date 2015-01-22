# Exercise 2 - Two-dimensional Random Walk

In this exercise, you will write a two-dimensional [random walk][] simulator.
The walk starts at the origin (0, 0).
At each time point, the walker randomly selects a direction (up, down, left, or
right) and moves one step in that direction. The walk is symmetric if all
directions have equal probability.

The goals of the exercise are:

* Become accustomed to using Numpy's array and random number generation
  facilities
* Learn about functions, function parameters, and default arguments
* Practice incremental development

You may need to consult the [Python][] and [Numpy][] documentation to complete
this exercise.

A template file, `random_walk.py`, has been provided. As you work through the
tasks and modify the template file, you can load your work in IPython with the
command

    %run random_walk.py

and then test your code by calling the corresponding function directly. For
example,

    x, y = random_walk(10)

The template also includes a function `draw_walk()` which will animate the path
traced out by the walk; it may be helpful for testing and entertainment
purposes.

## Task 1

Fill in the function `random_walk()`, which accepts an arbitrary number of
steps to take and returns x and y coordinates of the walker at each step. These
should be Numpy arrays, and should include the starting position (0, 0). The 
following algorithm is suggested:

1. Randomly sample the direction moved at each step. See the `numpy.random`
   submodule.
2. Convert the sampled directions into moves (e.g., up is a (0, 1) move).
    + Preallocate arrays for storing the moves with `numpy.zeros()`.
    + The `numpy.where()` function may prove useful here.
    + Consider storing moves in the x direction and moves in the y direction in
      separate arrays.
3. Use cumulative summation of the moves to calculate the x and y coordinates.

## Task 2

Modify the `random_walk()` function to accept a starting position parameters
`x_start` and `y_start`:

    def random_walk(n, x_start, y_start):
        # < your code >
        return x, y

Adjust the body of the function to take the starting position of the walk into
account. 

Make the `random_walk()` function start at the origin (0, 0) when
`x_start` and `y_start` are not specified by adding default arguments:

    def random_walk(n, x_start = 0, y_start = 0)
        # < your code >
        return x, y

Test that the function still works correctly.

## Task 3

Add a `p` parameter to `random_walk()`, where `p` is a vector of probabilities
for up, down, left, and right. Modify the body of the function to take this
parameter into account.

When `p` is not specified, default to a symmetric random walk. You could use
`numpy.ones()` and vectorization for this, but there are other possibilities as
well.

Once again, test that the function behaves as expected.

# Bonus Task

Use `if` statements to check that `p` has length 4 and sums to 1. If either of
these conditions are not true, [raise an exception][exception]:

    raise ValueError('p does not have length 4!')

[random walk]: https://en.wikipedia.org/wiki/Random_walk
[Python]: https://docs.python.org/3/tutorial
[Numpy]: http://docs.scipy.org/doc/numpy/reference
[exception]: http://stackoverflow.com/questions/2052390/how-do-i-manually-throw-raise-an-exception-in-python


