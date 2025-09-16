# test the conditions for factorial,
# prime number and area of circle with passing wrong parameters as 0
#using the unittest module
import unittest
from mymath import factorial, is_prime, area_of_circle

class TestMathFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)

    def test_prime_number(self):
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(0))

    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(4), 50.27, places=2)
        self.assertEqual(area_of_circle(0), 0)
        with self.assertRaises(ValueError):
            area_of_circle(-5)

if __name__ == "__main__":
    unittest.main()

