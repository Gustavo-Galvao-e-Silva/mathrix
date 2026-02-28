from __future__ import annotations
from typing import Iterator


class Vector:
    """
    A mathematical vector for linear algebra operations.

    A vector is an ordered collection of numbers representing a point or
    direction in n-dimensional space. Vectors are fundamental objects in
    linear algebra used to represent quantities with magnitude and direction.

    Parameters
    ----------
    data : list[int | float]
        A list of numbers representing the vector components.

    Attributes
    ----------
    data : list[int | float]
        The underlying list of vector components.
    shape : tuple[int, int]
        The dimensions of the vector as (dims, 1).

    Raises
    ------
    TypeError
        If data is not a list, or contains non-numeric elements.

    Examples
    --------
    >>> v = Vector([1, 2, 3])
    >>> print(v.dims)
    3
    >>> print(v)
    [1, 2, 3]
    """

    def __init__(self, data: list[int | float]) -> None:
        if not isinstance(data, list):
            raise TypeError(f"Vector data must be a list. Got {type(data).__name__}.")

        for i, x in enumerate(data):
            if not isinstance(x, (int, float)):
                raise TypeError(
                    f"All vector components must be numbers (int or float). "
                    f"Got {type(x).__name__} at index {i}."
                )

        self.data = data
        self.shape = (len(data), 1)

    def __getitem__(self, key: int) -> int | float:
        """
        Access a vector component by index.

        Parameters
        ----------
        key : int
            The index (0-based) of the component to access.

        Returns
        -------
        int | float
            The value at the specified index.

        Raises
        ------
        TypeError
            If key is not an integer.

        Examples
        --------
        >>> v = Vector([10, 20, 30])
        >>> v[0]
        10
        >>> v[2]
        30
        """
        if not isinstance(key, int):
            raise TypeError(
                f"Vector index must be an integer. Got {type(key).__name__}."
            )

        return self.data[key]

    def __setitem__(self, key: int, new_value: int | float) -> None:
        """
        Set a vector component at a specific index.

        Parameters
        ----------
        key : int
            The index (0-based) of the component to modify.
        new_value : int | float
            The new value to assign.

        Raises
        ------
        TypeError
            If key is not an integer or new_value is not a number.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> v[1] = 5
        >>> print(v)
        [1, 5, 3]
        """
        if not isinstance(key, int):
            raise TypeError(
                f"Vector index must be an integer. Got {type(key).__name__}."
            )

        if not isinstance(new_value, (int, float)):
            raise TypeError(
                f"Vector components must be numbers (int or float). "
                f"Got {type(new_value).__name__}."
            )

        self.data[key] = new_value

    def __len__(self) -> int:
        """
        Get the number of components in the vector.

        Returns
        -------
        int
            The dimension of the vector.

        Examples
        --------
        >>> v = Vector([1, 2, 3, 4])
        >>> len(v)
        4
        """
        return self.dims

    def __iter__(self) -> Iterator:
        """
        Iterate over the vector components.

        Returns
        -------
        Iterator
            Iterator over vector components.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> for component in v:
        ...     print(component)
        1
        2
        3
        """
        return iter(self.data)

    def __add__(self, other: Vector) -> Vector:
        """
        Add two vectors component-wise.

        Vector addition requires both vectors to have the same dimension.

        Parameters
        ----------
        other : Vector
            The vector to add.

        Returns
        -------
        Vector
            The sum of the two vectors.

        Raises
        ------
        TypeError
            If other is not a Vector.
        ValueError
            If the vectors have different dimensions.

        Examples
        --------
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v3 = v1 + v2
        >>> print(v3)
        [5, 7, 9]
        """
        if not isinstance(other, Vector):
            raise TypeError(
                f"Cannot add Vector and {type(other).__name__}. "
                f"Both operands must be vectors."
            )

        if self.dims != other.dims:
            raise ValueError(
                f"Cannot add vectors with different dimensions. "
                f"Left vector has {self.dims} dimensions, "
                f"right vector has {other.dims} dimensions."
            )

        result = []
        for i in range(self.dims):
            result.append(self[i] + other[i])

        return Vector(result)

    def __sub__(self, other: Vector) -> Vector:
        """
        Subtract one vector from another component-wise.

        Vector subtraction requires both vectors to have the same dimension.

        Parameters
        ----------
        other : Vector
            The vector to subtract.

        Returns
        -------
        Vector
            The difference of the two vectors.

        Raises
        ------
        TypeError
            If other is not a Vector.
        ValueError
            If the vectors have different dimensions.

        Examples
        --------
        >>> v1 = Vector([5, 7, 9])
        >>> v2 = Vector([1, 2, 3])
        >>> v3 = v1 - v2
        >>> print(v3)
        [4, 5, 6]
        """
        if not isinstance(other, Vector):
            raise TypeError(
                f"Cannot subtract {type(other).__name__} from Vector. "
                f"Both operands must be vectors."
            )

        if self.dims != other.dims:
            raise ValueError(
                f"Cannot subtract vectors with different dimensions. "
                f"Left vector has {self.dims} dimensions, "
                f"right vector has {other.dims} dimensions."
            )

        result = []
        for i in range(self.dims):
            result.append(self[i] - other[i])

        return Vector(result)

    def __rmul__(self, other: int | float) -> Vector:
        """
        Multiply vector by a scalar (from the left).

        Allows scalar multiplication in the form: scalar * vector

        Parameters
        ----------
        other : int | float
            The scalar to multiply by.

        Returns
        -------
        Vector
            The result of scalar multiplication.

        Raises
        ------
        TypeError
            If other is not a number.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> result = 3 * v
        >>> print(result)
        [3, 6, 9]
        """
        if not isinstance(other, (int, float)):
            return NotImplemented

        result = []
        for i in range(self.dims):
            result.append(self[i] * other)

        return Vector(result)

    def __truediv__(self, other: int | float) -> Vector:
        """
        Divide vector by a scalar.

        Divides each component of the vector by the scalar value.

        Parameters
        ----------
        other : int | float
            The scalar to divide by.

        Returns
        -------
        Vector
            The result of scalar division.

        Raises
        ------
        TypeError
            If other is not a number.
        ZeroDivisionError
            If other is zero.

        Examples
        --------
        >>> v = Vector([6, 9, 12])
        >>> result = v / 3
        >>> print(result)
        [2.0, 3.0, 4.0]
        """
        if not isinstance(other, (int, float)):
            return NotImplemented

        if other == 0:
            raise ZeroDivisionError("Cannot divide a vector by zero.")

        result = []
        for i in range(self.dims):
            result.append(self[i] / other)

        return Vector(result)

    def __neg__(self) -> Vector:
        """
        Negate the vector (multiply by -1).

        Returns
        -------
        Vector
            The negated vector.

        Examples
        --------
        >>> v = Vector([1, -2, 3])
        >>> neg_v = -v
        >>> print(neg_v)
        [-1, 2, -3]
        """
        return -1 * self

    def __eq__(self, other: object) -> bool:
        """
        Check if two vectors are equal.

        Vectors are equal if they have the same dimension and all
        corresponding components are equal.

        Parameters
        ----------
        other : object
            The object to compare with.

        Returns
        -------
        bool
            True if vectors are equal, False otherwise.

        Examples
        --------
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([1, 2, 3])
        >>> v1 == v2
        True
        """
        if not isinstance(other, Vector):
            return NotImplemented

        return self.data == other.data

    def __str__(self) -> str:
        """
        Return a string representation of the vector.

        Returns
        -------
        str
            String representation showing the vector components.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> print(v)
        [1, 2, 3]
        """
        return f"{self.data}"

    def __repr__(self) -> str:
        """
        Return a constructor-style string for data inspection.

        Returns
        -------
        str
            A string that could be used to recreate this vector.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> repr(v)
        'Vector([1, 2, 3])'
        """
        return f"Vector({self.data})"

    @property
    def dims(self) -> int:
        """
        Get the dimension of the vector.

        Returns
        -------
        int
            The number of components in the vector.

        Examples
        --------
        >>> v = Vector([1, 2, 3, 4, 5])
        >>> v.dims
        5
        """
        return self.shape[0]

    @property
    def magnitude(self) -> float:
        """
        Calculate the magnitude (length) of the vector.

        The magnitude is the Euclidean norm, computed as the square root
        of the sum of squared components.

        Returns
        -------
        float
            The magnitude of the vector.

        Examples
        --------
        >>> v = Vector([3, 4])
        >>> v.magnitude
        5.0
        >>> v2 = Vector([1, 0, 0])
        >>> v2.magnitude
        1.0
        """
        return (sum(val**2 for val in self.data)) ** 0.5

    def normalize(self) -> Vector:
        """
        Compute the unit vector in the same direction.

        A unit vector has magnitude 1 and points in the same direction
        as the original vector.

        Returns
        -------
        Vector
            The normalized vector (magnitude = 1).

        Raises
        ------
        ZeroDivisionError
            If the vector has zero magnitude.

        Examples
        --------
        >>> v = Vector([3, 4])
        >>> normalized = v.normalize()
        >>> print(normalized)
        [0.6, 0.8]
        >>> normalized.magnitude
        1.0
        """
        if self.magnitude == 0:
            raise ZeroDivisionError(
                "Cannot normalize a zero vector. " "The zero vector has no direction."
            )

        return self / self.magnitude

    def copy(self) -> Vector:
        """
        Create a deep copy of the vector.

        Returns
        -------
        Vector
            A new Vector object with the same components.

        Examples
        --------
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = v1.copy()
        >>> v2[0] = 99
        >>> print(v1[0])
        1
        """
        return Vector(self.data.copy())

    def to_list(self) -> list[int | float]:
        """
        Convert the vector to a list.

        Returns
        -------
        list[int | float]
            A copy of the vector components as a list.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> v.to_list()
        [1, 2, 3]
        """
        return self.data.copy()

    def to_tuple(self) -> tuple[int | float, ...]:
        """
        Convert the vector to a tuple.

        Returns
        -------
        tuple[int | float, ...]
            The vector components as a tuple.

        Examples
        --------
        >>> v = Vector([1, 2, 3])
        >>> v.to_tuple()
        (1, 2, 3)
        """
        return tuple(self)
