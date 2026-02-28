# panchi

**panchi** is a Python-native linear algebra library designed for learning, experimentation, and visual intuition.

The goal is not performance. The goal is **clarity**.

If you have ever used NumPy or SciPy and wondered *what the library is actually doing*, panchi is for you. Every algorithm is implemented directly in readable Python, every operation returns something you can inspect, and error messages are written to teach rather than just report.

---

## Where to start

If you are new to panchi, begin with the [Quickstart](getting-started/quickstart.md) — it covers the core ideas in a few minutes.

If you are looking for a specific function or class, go straight to the [API Reference](api/panchi.md).

If you want to understand the concepts behind the code, the [User Guide](user-guide/vectors.md) walks through each part of the library with worked examples and mathematical context.

---

## What panchi covers

- `Vector` and `Matrix` primitives with natural operator syntax
- Factory functions: identity, zero, diagonal, rotation matrices, and more
- Elementary row operations as first-class objects
- Row reduction to REF and RREF with full step-by-step output
- LU decomposition with partial pivoting
- Matrix inverse and linear system solving
- 2D visualization via Matplotlib, with optional Manim backend
