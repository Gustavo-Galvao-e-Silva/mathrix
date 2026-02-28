# Quickstart

This page gives you a feel for the library in a few minutes. For deeper explanations of any topic, follow the links into the User Guide.

## Vectors

```python
import panchi as pan

v = pan.Vector([3, 4])
print(v.magnitude)   # 5.0
print(v.normalize()) # [0.6, 0.8]

u = pan.Vector([1, 2, 3])
w = pan.Vector([4, 5, 6])
print(pan.dot(u, w))   # 32
print(pan.cross(u, w)) # [-3, 6, -3]
```

Vectors support the arithmetic you would expect: `+`, `-`, `*` and `/` with scalars, and unary `-` for negation.

## Matrices

```python
A = pan.Matrix([[1, 2], [3, 4]])
B = pan.Matrix([[5, 6], [7, 8]])

print(A @ B)          # matrix multiplication
print(A.T)            # transpose
print(A.trace)        # 5
print(A.determinant)  # -2.0
```

`@` is matrix multiplication. `*` is scalar multiplication. This matches standard Python convention and avoids ambiguity.

## Factory functions

```python
I = pan.identity(3)
Z = pan.zero_matrix(2, 3)
D = pan.diagonal([1, 2, 3])
R = pan.rotation_matrix_2d(3.14159 / 2)
```

## Algorithms

panchi's algorithms return result objects that carry the answer and the work behind it.

```python
from panchi.algorithms import rref, solve

A = pan.Matrix([[1, 2, 3], [2, 5, 7], [0, 1, 2]])

# Row reduction
reduction = rref(A)
print(reduction.rank)    # 3
print(reduction.result)  # the RREF matrix
print(reduction)         # full step-by-step walkthrough

# Solving a linear system
b = pan.Vector([1, 0, 0])
result = solve(A, b)
print(result.status)     # 'unique'
print(result.solution)   # solution vector x
```

From here, explore the [User Guide](../user-guide/vectors.md) for the concepts behind each part of the library.
