"""
assert is a keyword that we verify that the statement is true
will check assert for testing
"""
from program113 import square

def main():
    test_square()
    
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 sqaure is not equal 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 sqaure is not equal 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 sqaure is not equal 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 sqaure is not equal 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 sqaure is not equal 0")
        
if __name__ == "__main__":    
    main()