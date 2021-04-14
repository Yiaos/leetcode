# coding: utf-8
lst = [3,23,242,67,343,7,8,43,5,6,73,3,455]


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


# hello("Bob")


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
# print(example.__name__, example.__doc__)


def heap_sort(lst):
    if not lst:
        return []
    # 大顶堆
    for i in range((len(lst)-2)//2, -1, -1):
        shiftdown(i, lst, len(lst))
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        shiftdown(0, lst, i-1)

def shiftdown(root, lst, size):
    child = root * 2 + 1
    # 取较大子节点
    if child > size:
        return
    if child + 1 < size and lst[child] < lst[child+1]:
        child = child + 1
    # 交换
    if lst[child] > lst[root]:
        lst[child], lst[root] = lst[root], lst[child]
    root = child
    shiftdown(root, lst, size)

def fb(n):
    if n <= 2:
        return n
    else:
        return fb(n-1) + fb(n-2)

def fib(n):
    i = 3
    dp = [0]*(n+1)
    dp[1] = 1 
    dp[2] = 2
    while i < n+1:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]


arr = [[7],[3, 8], [8, 1, 0], [2, 7, 4, 4, ], [4, 5, 2, 6, 5]]

def get_max():
    max = 101
    dp = [[0]*len(arr) for _ in range(len(arr))]
    n = 5
    i = j = 0
    max_sum = get_max_num(dp, n, i, j)

def get_max_num(arr, n, i, j):
    if i == n:
        return arr[i][j]
    x = get_max_num(arr, n, i+1, j)
    y = get_max_num(arr, n, i+1, j+1)
    return max(x, y) + arr[i][j]


def get_max1():
    for i in range(n-1, 1, -1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
    return dp[i][j]


def best_time(nums):
    ans = 0
    min_price = nums[0]
    max_profit = 0
    for i in range(1, len(nums)):
        min_price = min(nums[i], min_price)
        max_profit = max(max_profit, nums[i] - min_price)
    return max_profit


class Queues():
    pass

from collections import deque

class Stack():
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.p = self.q1
    
    def switch(self):
        self.p = self.q1 if self.p == self.q2 else self.q2

    @property
    def another(self):
        return self.q1 if self.p == self.q2 else self.q2

    def push(self, x):
        self.p.append(x)        
        return

    @property
    def len(self):
        return len(self.p)

    def pop(self):
        if self.empty():
            return -1
        while self.len > 1:
            val = self.p.popleft()
            self.another.append(val)
        top = self.p.popleft()
        self.switch()
        return top

    def top(self):
        if self.empty():
            return -1
        return self.p[self.len-1]
    
    def empty(self):
        if self.len == 0:
            return True
        return False


def all(s):
    from collections import deque
    dq = deque()
    dq.append('')
    ans = []
    while dq:
        for letter in s:
            dq.append(letter)

def all(s):
    if len(s) <= 1:
        return [s]
    ans = []
    for i in range(len(s)):
        for j in all(s[:i]+s[i+1:]):
            ans.append(s[i] + j)
    return ans.sorted()


if __name__ == "__main__":
#     # ShellSort(lst)
#     # CountSort(lst)
    # heap_sort(lst)
    # HeapSort(lst)
    # print(fib(100))
    # print(lst)
    # print(best_time([7,6,4,3,1]))
    print(all("abc"))


# 1, 2, 3, 4, 5, 10, 11, 15, 17, 19, 20 ,21, 22, 23, 31, 32, 33, 34, 39,
# 42, 46, 48, 49, 53, 55, 56, 62, 64, 70, 72, 75, 79,
# # 76, 78, 84, 85,
# 94, 96, 98, 101, 102, 104, 105, 114, 121, 124, 128, 136, 139, 141
# 142, 146, 148， 152，155，160，169，198，200，206，207，208，215，221，
# 226，234，236，238，239，240，253，279，283，287，297，300，301，309，
# 312，322，337，338，347，394，399，406，416，437，438，448，461，494，
# 538，543，560，581，617，621，647，739