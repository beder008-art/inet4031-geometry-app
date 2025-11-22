import unittest
import math
import sphere


class sphereTest(unittest.TestCase):
    """Unit tests for sphere.volume(rad).

    Tests use assertAlmostEqual to avoid floating-point rounding issues.
    """

    def test_volume_zero(self):
        self.assertAlmostEqual(sphere.volume(0), 0.0, places=12)

    def test_volume_two(self):
        expected = (4.0 / 3.0) * math.pi * (2**3)
        self.assertAlmostEqual(sphere.volume(2), expected, places=12)

    def test_volume_ten(self):
        expected = (4.0 / 3.0) * math.pi * (10**3)
        self.assertAlmostEqual(sphere.volume(10), expected, places=12)


if __name__ == "__main__":
    unittest.main()
