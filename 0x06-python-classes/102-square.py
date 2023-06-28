#!/usr/bin/python3

"""
This module defines the Square class that represents a square shape.
"""


class Square:
    """
    This class defines a square object based on the provided size.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int, float): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int, float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int, float): The size value to be set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of self is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of self is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of self is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of self is less or equal, False otherwise.
        """
        return self.area() <= other.area()
