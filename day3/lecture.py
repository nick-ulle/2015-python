
# Today's Agenda:
#
# 1. Introduce NumPy
# 2. Simple random walk
# 3. Visualize SVD/PCA

a = [1, 2, 3]

# Python's lists are awesome, but they have a few serious limitations for
# numerical computing:
#
# 1. They use a lot of memory (~32 MB for 1 million 64-bit floats).
# 2. They're slow.
# 3. They're not vectorized. We could use list comprehensions, but do you
#    really want to write

[x + 5 for x in a]

#    instead of

a + 5

# So we need a better solution when we do numerical computing. Enter NumPy!

import numpy

# We're going to use NumPy all the time, so let's save some typing with an
# alias:

import numpy as np

# Using `np` for NumPy is a common convention.
# 
# You can convert a Python list to a NumPy array with `array()`.

np.array([1, 2])
b = np.array(a)

# DATA GOLF! A list of 1 million floats uses ~32 MB.
# How much memory does a NumPy array of 1 million floats use?

big_np_array = np.arange(1e6)
big_list = [float(x) for x in range(int(1e6))]

# NumPy also knows we want to do numerical work, where vectorized operations
# make sense.

b + 5

# These vectorized operations are also faster than corresponding operations on
# lists.

%timeit big_np_array + 5
%timeit [x + 5 for x in big_list]

# Indexing and slicing uses `[ ]`, the same as Python lists.

b[1:]

# WARNING: Python objects, including lists and NumPy arrays, are stored as
# references. Compared to R, they might not behave as you'd expect.

b_copy = b
b_copy[1] = 7

# What are the elements of `b_copy`? What're the elements of `b`?
b_copy
b

# ZEN: Explicit is better than implicit.
# If you wanted to make a copy, do it explicitly!

b = np.array(a)

b_copy = b.copy()
b_copy[1] = 7

b_copy
b

# Matrices can be defined directly

np.array([[1, 2], [3, 4]])

# or by reshaping an array

A = np.array([1, 2, 3, 4]).reshape(2, 2)
A

# How do you do matrix multiplication?
I = np.eye(2)
I

A * I

# Using `*` does element-by-element multiplication. Instead, call the `dot()`
# method  or `dot()` function.

A.dot(I)
np.dot(A, I)

# In Python 3.5, there will be an operator, `@`, for matrix multiplication.

# What else do we get with NumPy?
#
# * linear algebra (numpy.linalg)
# * random number generation (numpy.random)
# * Fourier transforms (numpy.fft)
# * polynomials (numpy.polynomial)

# Let's write a simple random walk!
#
# 1. Get the step (up or down) at each time. That is, take N independent
#    samples from a binomial(1, p) or Bernoulli(p) distribution.
# 2. Transform 0s to -1s (down).
# 3. Use cumulative sums to calculate the position at each time.

N = 10
p = 0.5
steps = np.random.binomial(1, p, N)

steps[steps == 0] = -1
steps

positions = steps.cumsum()

import matplotlib.pyplot as plt

# Turn on Matplotlib's interactive mode.
plt.ion()

plt.plot(positions)

# The SVD is a very important decomposition, especially to statistics.
# A great statistics example is Principal Components Analysis (PCA).
# What is PCA typically used for?

# Say X is a centered n-by-p data matrix. Then
#
# X = UDV' = λ₁u₁v₁' + ... + λₖuₖvₖ' + ... + λₚuₚvₚ'   (n < p)
#
# PCA takes the first k principal components, λ₁u₁, ..., λₖuₖ.
# A slightly different perspective: PCA approximates the original data by
#
# X ~ λ₁u₁v₁' + ... + λₖuₖvₖ'
#
# Lossy data compression!

# To load an image, use SciPy, Matplotlib, or Scikit-Image.
import skimage as ski, skimage.io

img = ski.io.imread('photo.png', as_grey=True)

plt.imshow(img).set_cmap('gray')

# Center the image and take the SVD.
mean = np.mean(img, axis=0)

ctr_img = img - mean

plt.imshow(ctr_img).set_cmap('gray')

_, _, v = np.linalg.svd(ctr_img)

# `linalg.svd()` returns V', not V.
v = v.T

# Remove some columns from V (terms in the SVD sum).
v_reduced = v[:, 0:100]
prin_comp = ctr_img.dot(v_reduced)

# Reconstruct the data.
reconst = np.dot(prin_comp, v_reduced.T) + mean

# Another way:
reconst = prin_comp.dot(v_reduced.T) + mean

fig, axs = plt.subplots(1, 2)
for ax, im in zip(axs, [img, reconst]):
    ax.imshow(im).set_cmap('gray')
fig.show()

# DATA GOLF! How much compression?
# Original image: 

original_size = img.size

# Compressed image:

compressed_size = mean.size + v_reduced.size + prin_comp.size

compressed_size / original_size

