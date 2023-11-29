"""
pytest - this is third party tool for the testing
"""
import pytest
from program113 import square

def test_postive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# using the below code we can test the string weather they will work or not
def test_str():
    with pytest.raises(TypeError):
        square("cat")