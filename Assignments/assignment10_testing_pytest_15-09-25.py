# test the conditions for factorial,
# prime number and area of circle with passing wrong parameters as 0
#using the pytest module
import pytest
from mymath import factorial, is_prime, area_of_circle

def test_factorial():
    assert factorial(4) == 24
    assert factorial(0) == 1

def test_prime_number():
    assert is_prime(31) == True
    assert is_prime(17) == True
    assert is_prime(0) == False

def test_area_of_circle():
    assert area_of_circle(4) == pytest.approx(50.27, rel=1e-2)
    assert area_of_circle(0) == 0
    with pytest.raises(ValueError):
        area_of_circle(-5)
