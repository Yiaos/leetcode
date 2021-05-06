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
    if n <= 2:
        return 1
    i = 3
    dp = [0]*(n+1)
    dp[1] = 1 
    dp[2] = 1
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

def add(a, b):
    return a+b

# input = input().split()
# a=int(input[0])
# b=int(input[1])
# print(add(a,b))

# def max_p(lst_n, lst_k):
#     n = len(lst_n)
#     lst_n.sort()
#     k = len(lst_k)
#     lst_k.sort()
#     solved = 0
#     i, j = 0, 0
#     while i < n and j < k:
#         if lst_n[i] > lst_k[j]:
#             j += 1
#         else:
#             solved += 1
#             i += 1
#             j += 1
#     return solved

def search_log(logs_dict, start, end,_type, min_ts):
    logs = logs_dict.get(_type, [])
    if not logs:
        return 0
    count = 0
    n = len(logs)
    end = min(end-min_ts, n)
    start = 0 if start<min_ts else start-min_ts
    while start <= end:
        count += logs[start]
        start += 1
    return count


if __name__ == "__main__":
    n_m = [int(x) for x in input().split()]
    n = n_m[0]
    m = n_m[1]
    tmp_dict = {}
    row = input().split()
    _ts, _type, _times = int(row[0]), row[1], int(row[2])
    min_ts = _ts
    for i in range(n):
        if _type in tmp_dict:
            lst = tmp_dict[_type]
            lst[_ts-min_ts] += _times
        else:
            lst = [0] * 100000
            lst[_ts-min_ts] = _times
            tmp_dict[_type] = lst
        if i == n-1:
            break 
        row = input().split()
        _ts, _type, _times = int(row[0]), row[1], int(row[2])
    for _ in range(m):
        s_e = input().split()
        start = int(s_e[0])
        end = int(s_e[1])
        _type = s_e[2]
        print(search_log(tmp_dict, start, end, _type, min_ts))


# def search(size, logs, start, end):
#     count = 0
#     for i in range(size):
#         if start <= logs[i] <= end:
#             count += 1
#         else:
#             continue
#     return count

def bin_search(n, logs, start, end):
    l, r = 0, n-1
    
    while l < r:
        mid = (l+r)//2
        if logs[mid] >= start:
            r = mid
        else:
            l = mid + 1
    s = l
    l, r = 0, n-1
    while l < r:
        mid = (l+r+1)//2
        if logs[mid] <= end:
            l = mid
        else:
            r = mid -1
    return r - s + 1


# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         logs = []
#         for i in range(n):
#             logs.append(int(input()))
#         m = int(input())
#         for j in range(m):
#             _range = [int(x) for x in input().split()] 
#             print(bin_search(n, logs, _range[0], _range[1]))


# def tree_sum(nums):
#     tmp = {}
#     ans = 0
#     for num in nums:
#         mod = num % 3
#         tmp[mod] = tmp.get(mod, 0) + 1
#     return tmp.get(0, 0) + min(tmp.get(1, 0), tmp.get(2,0)) + \
#          abs(tmp.get(1, 0) - tmp.get(2, 0)) // 3
    

# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         nums = [int(x) for x in input().split()]
#         print(tree_sum(nums))

# import base64
# def b64to36(b64_str):
#     _str = base64.b64decode(b64_str)
#     n = len(_str)
#     dec_num = 0
#     for i, s in enumerate(_str):
#         dec_num += 256**(n-i-1) * s
    
#     proced_36 = []
#     x, y = divmod(dec_num, 36)
#     while x > 0:
#         if y >= 10:
#             y = chr(y+55)
#         else:
#             y = str(y)
#         proced_36.append(y)
#         x, y = divmod(x, 36)
#     if y >= 10:
#         y = chr(y+55)
#     else:
#         y = str(y)
#     proced_36.append(y)
#     return "".join(proced_36[::-1])
    

# def get_d(n, e):
#     p = 10007
#     q = 23333
#     # 欧拉函数x
#     x = (p-1) * (q-1)
#     k = 1
#     # 计算d
#     d = extend_gcd(x, e)
#     return d

# def extend_gcd(x, e):
#     if x < e:
#         e, x = x, e
    
#     x1, x2, x3 = 1, 0, x
#     y1, y2, y3 = 0, 1, e
#     while True:
#         # x, e不互素
#         if y3 == 0:
#             return None
#             break
#         elif y3 == 1:
#             return y2 % x
#             break
#         else:
#             a = x3 // y3
#             t1, t2, t3 = x1 - a * y1, x2 - a * y2, x3 - a * y3
#             x1, x2, x3 = y1, y2, y3
#             y1, y2, y3 = t1, t2, t3


# if __name__ == "__main__":
#     row = input().split()
#     e = int(row[0])
#     c = int(row[1])
#     n = 23333*10007
#     d = get_d(n, e)
#     m = pow(c, d, n)
#     print(m)


# 4 2
# 1 1 1 1
def wait_time(n, m, time_lst):
    drinking = []
    drinking_tmp = []
    if n < m:
        print(0)
    elif n == m:
        print(min(time_lst)+1)
    else:
        for i in range(0, m):
            drinking.append(time_lst[i])
            drinking_tmp.append(time_lst[i])
        tmp = min(sorted(drinking))
        index = m - 1

        d_sumtime = {i: j for i, j in enumerate(time_lst[0:m])}

        while index < n - 1:
            for i in range(0, m):
                if drinking[i] > 0:
                    drinking[i] -= tmp
                    if drinking[i] == 0 and index < n - 1:
                        index += 1

                        drinking[i] = time_lst[index]
                        drinking_tmp[i] = time_lst[index]
                        d_sumtime[i] += drinking_tmp[i]
                elif drinking[i] == 0 and index < n - 1:

                    index += 1

                    drinking[i] = time_lst[index]
                    drinking_tmp[i] = time_lst[index]
                    d_sumtime[i] += drinking_tmp[i]

            tmp = min(sorted(drinking))

        return min(*d_sumtime.values())+1


if __name__ == "__main__":
    firstrow = input().split()
    n = int(firstrow[0])
    m = int(firstrow[1])
    time_lst = [int(x) for x in input().split()]
    print(wait_time(n, m, time_lst))


# 1, 2, 3, 4, 5, 10, 11, 15, 17, 19, 20 ,21, 22, 23, 31, 32, 33, 34, 39,
# 42, 46, 48, 49, 53, 55, 56, 62, 64, 70, 72, 75, 79,
# # 76, 78, 84, 85,
# 94, 96, 98, 101, 102, 104, 105, 114, 121, 124, 128, 136, 139, 141
# 142, 146, 148， 152，155，160，169，198，200，206，207，208，215，221，
# 226，234，236，238，239，240，253，279，283，287，297，300，301，309，
# 312，322，337，338，347，394，399，406，416，437，438，448，461，494，
# 538，543，560，581，617，621，647，739