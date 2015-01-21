
1 million floating point values in a list: 24 - 32 MB (should be 8 MB)

1. Lists take up too much memory!
2. We'd like to have vectorization.
3. Lists are kind of slow.

NumPy provides an alternative: the n-dimensional array.

DATA GOLF!
How much memory does a 1 million element ndarray of floats use?
8 MB!

NumPy takes 8.6 ms to add 5 to 1 million element ndarray.
Python lists take 501ms!

Be careful with references! 

We saw NumPy gives us arrays, matrices, ... But what else?

* random number generation (numpy.random)
* fast Fourier transforms (numpy.fft)
* polynomials (numpy.polynomial)
* linear algebra (numpy.linalg)
* support for calling C libraries

# Simple Random Walk!

Random walk with 100 steps

1. Flip a coin 100 times--these are the steps (0 means down).
2. Take cumulative sums

# PCA / SVD
The SVD is a very important decomposition, especially to statistics.
A great statistics example is Principal Components Analysis (PCA).
What is PCA typically used for?

Say X is a centered n-by-p data matrix. Then

X = UDV' = λ₁u₁v₁' + ... + λₖuₖvₖ' + ... + λₚuₚvₚ'   (n < p)

PCA takes the first k principal components, λ₁u₁, ..., λₖuₖ.
A slightly different perspective: PCA approximates the original data by

X ~ λ₁u₁v₁' + ... + λₖuₖvₖ'

Lossy data compression!

DATA GOLF!
Original image: 180,500
Compressed image: 86,461
