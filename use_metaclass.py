class SingleTon(type):
    def __init__(cls,  name, bases, dict):
        super[SingleTon, cls].__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__call__(*args, **kwargs)
        return cls._instance

class TestClass(object):
    __metaclass__ = SingleTon

test1 = TestClass()
test2 = TestClass()
test1.a = 2
print test1.a, test2.a
print id(test1), id(test2)