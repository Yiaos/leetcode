#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 1. 栈
        # l = list()
        
        # mapping = {
        #     "}": "{",
        #     ")": "(",
        #     "]": "["
        # }
        # for i in s:
        #     if i in ('{', '(', '['):
        #         l.append(i)
        #     elif len(l) > 0 and l[-1] == mapping[i]:
        #         l.pop()
        #     else:
        #         return False
        # if len(l) != 0:
        #     return False
        # return True

        # 2. replace
        while len(s) > 0:
            l = len(s)
            s=s.replace("{}","").replace("[]","").replace("()", "")
            if l == len(s):
                return False
        return True
s=Solution()
print(s.isValid("()"))

# @lc code=end

