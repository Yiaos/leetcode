#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈
        # stack = [-1,]
        # n = len(s)
        # ans = 0
        # for i in range(n):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #         else:
        #             ans = max(ans, i - stack[-1])
        # return ans

        # 动态规划
        n = len(s)
        ans = 0
        dp = [0] * n 
        for i in range(1, n):
            if s[i] == ')':
            # ()()
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                # (())
                # i-dp[i-1]-1 :the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
                ans = max(ans, dp[i])
        return ans

s=Solution()
print(s.longestValidParentheses(')()())'))
# @lc code=end

