#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # # 1. 动态规划
        # if not s:
        #     return 0
        # # 无法解码
        # if s[0] == '0':
        #     return 0
        # dp = [0] * (len(s)+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(1, len(s)):
        #     if s[i] == '0':
        #         # 10 或 20, 一种解码方式, 解码总数不改变
        #         if s[i-1]  in ('1', '2'):
        #             dp[i+1] = dp[i-1]
        #         else:
        #             return 0
        #     # 10 - 26, 两种
        #     elif s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
        #         dp[i+1] = dp[i-1] + dp[i]
        #     else:
        #         # 一种
        #         dp[i+1] = dp[i]
        # return dp[-1]

        # 2. 动态规划 - 滑动数组优化
        if not s:
            return 0
        # 无法解码
        if s[0] == '0':
            return 0
        cur = pre = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                # 10 或 20, 一种解码方式, 解码总数不改变
                if s[i-1] in ('1', '2'):
                    cur = pre
                else:
                    return 0
            # 10 - 26, 两种
            elif s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                pre, cur = cur, (cur + pre)
            else:
                # 一种
                pre = cur
                
        return cur
        
s=Solution()
print(s.numDecodings("123123"))
# @lc code=end

