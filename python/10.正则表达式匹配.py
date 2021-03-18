#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    cache = {}
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划 + 回溯
        if not p:
            return not s

        if (s,p) in self.cache:
            return self.cache[(s,p)] 
        # * 结尾
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s,p)] = True
                return True
            #    
            if s and p[-2] in ('.', s[-1]):
                if self.isMatch(s[:-1], p):
                    self.cache[(s,p)] = True
                    return True

        if s and p[-1] in (s[-1], '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s,p)] = True
            return True

        self.cache[(s,p)] = False
        return False


        # # 动态规划
        # # 如果p最后一个字符和s不匹配，则dp[i][j] = False
        # # 如果p最后一个字符是*, 则 dp[i][j] = dp[i][j-1]， 将*排除
        # # 如果s和p最后一个字符匹配，则dp[i][j] = d[i-1]dp[j-1], 将两个字符排除
        # def match(i , j):
        #     # s为空
        #     if i == 0:
        #         return False
        #     if p[j-1] == '.':
        #         return True
        #     return s[i-1] == p[j-1]
        # 
        # dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        # dp[0][0] = True
        # for i in range(len(s)+1):
        #     for j in range(1, len(p)+1):
        #         if p[j-1] == '*':
        #             dp[i][j] |= dp[i][j-2]
        #             if match(i, j-1):
        #                 dp[i][j] |= dp[i-1][j]
        #         else:
        #             if match(i, j):
        #                 dp[i][j] |= dp[i-1][j-1]
        # return dp[len(s)][len(p)]


        # # 暴力求解， 简单易懂， 牛
        # if not p:
        #     return not s
        # first_match = bool(s) and p[0] in (s[0], '.')
        # if len(p) >= 2 and p[1] == '*':
        #     # 匹配0次或1次以上
        #     return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])


s = Solution()
print(s.isMatch(s='aa',p='a*'))

# @lc code=end

