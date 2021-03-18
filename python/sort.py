# coding: utf-8
lst = [3,23,242,67,343,3,7,8,43,5,6,73,3,455]


def swap(lst, x, y):
    lst[x], lst[y] = lst[y], lst[x]


def ShellSort(lst):
    gap = len(lst) // 2
    while gap >= 1:
        for i in range(gap, len(lst)):
            j = i
            while j - gap >= 0 and lst[j-gap] > lst[j]:
                swap(lst, j, j-gap)
                j -= gap
        gap //= 2
    

def CountSort(lst):
    minNum = maxNum = lst[0]
    for num in lst:
        minNum = num if num < minNum else minNum
        maxNum = num if num > maxNum else maxNum
    
    tmpList = [0] * (maxNum - minNum + 1)
    for i in lst:
        tmpList[i - minNum] += 1
    k = 0
    for i in range(len(tmpList)):
        if tmpList[i] == 0:
            continue
        for _ in range(tmpList[i]):
            lst[k] = i + minNum
            k += 1


def HeapSort(lst):
    for i in range((len(lst) - 2) // 2, -1, -1):
        buildMaxHeap(lst, len(lst) , i)
    
    for i in range(len(lst) - 1, 0, -1):
        swap(lst, 0, i)
        buildMaxHeap(lst, i - 1, 0)



def buildMaxHeap(lst, size, root):
    while True:
        child = root * 2 + 1
        if child >= size:
            break
        if child + 1 < size and lst[child] < lst[child + 1]:
            child += 1
        if lst[child] > lst[root]:
            swap(lst, child, root)
            root = child
        else:
            break



# 1.使用__new__方法
class Singleton(object):
    _instance = None
    def __init__(self):
        pass
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

# s1 = Singleton()
# s2 = Singleton()
# print(id(s1)==id(s2))
    

# 2.使用函数装饰器
def singleton(cls):
    _instance={}
    def _new():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return _new

@singleton
def func():
    pass

# f1 = func()
# f2 = func()
# print(id(f1)==id(f2))


# 3.使用类装饰器
class Singleton2(object):
    def __init__(self, cls):
        self._instance = {}
        self._cls = cls

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton2
def func2():
    pass

# f3 = func2()
# f4 = func2()
# print(id(f3)==id(f4))

# 4.使用metaclss实现
class Singleton3(type):
    _instance = {}
    def __call__(cls, *args, **kw):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton3, cls).__call__(*args, **kw)
        return cls._instance


# class Cls(metaclass=Singleton3):
#     pass

# c1 = Cls()
# c2 = Cls()
# print(id(c1)==id(c2))
        

def logging(level):
    def wrapper(func):
        from functools import wraps
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("level:%s, func:%s" %(level, func.__name__))
            func(*args, **kwargs)
            print("over")
        return inner_wrapper
    return wrapper

@logging('info')
def hello(who):
    print("hello %s func:%s" % (who,hello.__name__))


hello("Bob")


from functools import wraps   
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper  

@my_decorator 
def example():
    """Docstring""" 
    print('Called example function')
print(example.__name__, example.__doc__)



# if __name__ == "__main__":
#     # ShellSort(lst)
#     # CountSort(lst)
#     # HeapSort(lst)
#     # print(lst)

# 1, 2, 3, 4, 5, 10, 11, 15, 17, 19, 20 ,21, 22, 23, 31, 32, 33, 34, 39,
# 42, 46, 48, 49, 523, 55, 56, 62, 64, 70, 72, 75, 76, 78, 79, 84, 85,
# 94, 96, 98, 101, 102, 104, 105, 114, 121, 124, 128, 136, 139, 141