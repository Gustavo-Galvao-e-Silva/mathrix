# Decompositions

A matrix decomposition factors a matrix into simpler pieces that reveal its structure. panchi currently implements LU decomposition with partial pivoting.

## LU Decomposition

LU decomposition factors a square matrix A into a lower triangular matrix L and an upper triangular matrix U. Because row swaps are often necessary for numerical stability, panchi uses **partial pivoting**, which introduces a permutation matrix P:

$$P A = L U$$

```python
import panchi as pan
from panchi.algorithms import lu

A = pan.Matrix([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 10]])

decomp = lu(A)

print(decomp.lower)        # L — lower triangular, ones on diagonal
print(decomp.upper)        # U — upper triangular
print(decomp.permutation)  # P — encodes the row swaps made
```

The decomposition satisfies the invariant `P @ A == L @ U`:

```python
assert decomp.permutation @ A == decomp.lower @ decomp.upper
```

## The LUDecomposition object

`lu()` returns an `LUDecomposition` result object:

```python
decomp.original     # the original matrix A
decomp.lower        # L
decomp.upper        # U
decomp.permutation  # P
decomp.steps        # the row operations applied during elimination
```

Printing it gives a readable summary:

```python
print(decomp)
# LU decomposition of 3×3 matrix — 3 steps
#
# P @ A = L @ U
#
# P:
# ...
# L:
# ...
# U:
# ...
```

## What partial pivoting means

At each step of elimination, partial pivoting swaps rows so that the entry with the largest absolute value in the current pivot column becomes the pivot. This avoids division by small numbers and keeps the decomposition numerically well-behaved.

The row swaps are recorded in P, so the factorisation relationship remains exact even after pivoting.

## What L and U encode

U is the result of Gaussian elimination applied to P @ A — it is the REF of the permuted matrix. L encodes the elimination steps: each entry below the diagonal in column j of L is the scalar that was used to zero out that row's entry in column j.

This means the steps recorded in `decomp.steps` and the entries of L are two ways of reading the same information.
