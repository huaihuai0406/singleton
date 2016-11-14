def SingleTon(cls, *args, **kwargs):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton


@SingleTon
class TestClass(object):
    a = 1

test1 = TestClass()
test2 = TestClass()
print test1.a, test2.a

test1.a = 2
print test1.a, test2.a
print id(test1), id(test2)