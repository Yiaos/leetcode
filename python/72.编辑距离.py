#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]  i->word1前i个字符 变成 j->word2前j个字符 需要的步骤
        # m = len(word1)
        # n = len(word2)
        # if not m or not n:
        #     return m or n
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # for i in range(m+1):
        #     dp[i][0] = i
        # for j in range(n+1):
        #     dp[0][j] = j
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # return dp[-1][-1]

        # O(n)
        m, n = len(word1), len(word2)
        # 占用空间更小
        # if m < n:
        #     m, n = n, m
        #     word1, word2 = word2, word1

        curr = list(range(n+1))
        for i in range(m):
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                if word1[i] == word2[j]:
                    curr[j+1] = prev[j]
                else:
                    curr[j+1] = min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]

s=Solution()
print(s.minDistance(word1 = "horse", word2 = "ros"))
# @lc code=end

