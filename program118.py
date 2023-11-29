from program117 import hello

def test_default():
    hello() == "hello, world"

def test_argument():
    hello("David") == "hello, David"

def test_multiple_argument():
    for name in ["Manoj","Parul"]:
        assert hello(name) == f"hello,{name}"