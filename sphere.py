"""Small utility functions for sphere calculations.

Provides:
- surfaceArea(rad): return 4 * pi * r^2
- volume(rad): return (4/3) * pi * r^3

Designed to be minimal and easily unit-testable.
"""

import math


def surfaceArea(rad):
    """Return surface area of a sphere with radius `rad`.

    rad -- numeric radius (int/float)
    """
    return 4.0 * math.pi * (rad**2)


def volume(rad):
    """Return volume of a sphere with radius `rad`.

    Formula: (4/3) * pi * r^3
    """
    return (4.0 / 3.0) * math.pi * (rad**3)


def prompt():
    """Simple CLI prompt when run directly (keeps file runnable)."""
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\nThe Volume of a Sphere = ", volume(radius))


if __name__ == "__main__":
    prompt()
