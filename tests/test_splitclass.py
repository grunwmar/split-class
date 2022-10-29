import sys
sys.path.append('../../split-class')
from splitclass import splitclass, partialclass


def test_partial_decorator():
    """ TEST 1 - Testing function of @partialclass decorator """

    @partialclass
    class AnyObject:
        ...

    assert hasattr(AnyObject, "__partial__")
    assert AnyObject.__partial__ == True


def test_split_decorator_class_name():
    """ TEST 2 - Testing function of @splitclass decorator if class name is """
    """ exchanged properly """

    @splitclass
    class AnyObject:
        ...

    assert AnyObject.__name__ == "AnyObject"


def test_split_decorator_bases():
    """ TEST 3 - Testing function of @splitclass decorator is class bases are """
    """ exchanged properly """

    TestClass = type('TestClass', (), {})

    @splitclass
    class AnyObject(TestClass):
        ...

    assert AnyObject.__bases__ == (TestClass, )


def test_split_decorator_attributes():
    """ TEST 4 - Testing function of @splitclass decorator is loading @partialclass """
    """ marked classses properly """

    @splitclass
    class AnyObject:

        def __init__(self, name):
            self.name = name

    any_object = AnyObject('John')

    assert any_object.any_method() == 'Hello John'
    assert any_object.CONSTANT == '1234567890'
