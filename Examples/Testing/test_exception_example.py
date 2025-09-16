import pytest
from mymath import add, divide
 
def test_add():
    assert add(2,3) == 5
    assert isinstance(add(1,2), int)
   
def test_divide_by_zero():
    with pytest.raises(ValueError) as e:
        divide(1,0)
        assert "division" in str(e.value)
 
 