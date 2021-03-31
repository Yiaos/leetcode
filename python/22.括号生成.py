#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        # 0.暴力破解
        # def is_valid(p):
        #     bal = 0
        #     for _p in p:
        #         if _p == '(':
        #             bal += 1
        #         else:
        #             bal -= 1
        #             if bal < 0:
        #                 return False
        #     return bal == 0
        # def generate(p):
        #     if len(p) == 2*n:
        #         if is_valid(p):
        #             ans.append(''.join(p))
        #     else:
        #         p.append('(')
        #         generate(p)
        #         p.pop()
        #         p.append(')')
        #         generate(p)
        #         p.pop()
        # ans = []
        # generate([])
        # return ans
        
        # 1. 栈, 深度优先遍历 DFS Depth First Search
        # stack = [('', 0, 0)]
        # ans = list()
        # while stack:
        #     p, left, right = stack.pop()
        #     if left == right == n:
        #         ans.append(p)
        #         continue
            
        #     if left < n:
        #         stack.append((p+'(', left+1, right))
        #     if right < n and right < left:
        #         stack.append((p+')', left, right+1))
        # return ans

        # 2. 队列 广度优先遍历 BFS  Breadth First Search
        # import collections
        # dq = collections.deque()
        # ans = list()
        # dq.append(('', 0, 0))
        # while dq:
        #     p, left, right = dq.popleft()
        #     if left == right == n:
        #         ans.append(p)
        #         continue
            
        #     if left < n:
        #         dq.append((p+'(', left+1, right))
        #     if right < n and right < left:
        #         dq.append((p+')', left, right+1))
        # return ans

        # 3. 回溯， 深度优先
        ans = []
        def backtrack(p, left, right):
            if len(p) == 2*n:
                ans.append(''.join(p))
                return
            if left < n:
                p.append('(')
                backtrack(p, left+1, right)
                p.pop()
            if right < left:
                p.append(')')
                backtrack(p, left, right+1)
                p.pop()
            
        backtrack([], 0, 0)
        return ans

        # 4. 动态规划, 未实现
        # 任何一个合法的括号序列都由(开头，并且第一个(一定有唯一与之对应的)
        # 括号序列可以使用（A）B表示，A,B分别是一个合法的括号序列或空
        # 需要枚举与第一个(对应的)的位置2*i+1
        # 递归调用generate(i) 可以计算A的所有可能性
        # 递归调用generate(n-i-1) 可以计算出B的所有可能性
        # 遍历A和B的所有可能性并连接，即可得到所有长度为2*n的括号序列
        # if n == 0:
        #     return ['']
        # ans = []
        # for i in range(n):
        #     for left in self.generateParenthesis(i):
        #         for right in self.generateParenthesis(n-1-i):
        #             ans.append('({}){}'.format(left, right))
        # return ans

        # 5. yield  generate
        # def generate(p, left, right):
        #     if right >= left >= 0:
        #         if not right:
        #             yield p
        #         for q in generate(p+'(', left-1, right):
        #             yield p
        #         for q in generate(p+')', left, right-1):
        #             yield p
        # return list(generate('', n, n))

        # 6. tricks that I do not understard yet
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)

s = Solution()
print(s.generateParenthesis(3))

# @lc code=end

