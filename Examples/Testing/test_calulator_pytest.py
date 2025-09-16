import calculator
import pytest
 
def test_add():
    assert calculator.add(2,3) == 5
    assert calculator.add(-1,1) == 0
   
def test_subtract():
    assert calculator.subtract(2,3) == 1
   
def test_multiply():
    assert calculator.multiply(8,2) == 16
   
def test_divide(self):
    assert calculator.divide(10,5),2
    with pytest.raises(ValueError):
        calculator.divide(10,0)