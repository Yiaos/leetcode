#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 动态规划
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False

        # dp = [[False] * (n+1) for _ in range(m+1)]
        # dp[0][0] = True
        # for i in range(1, m+1):
        #     dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # for j in range(1, n+1):
        #     dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         dp[i][j] = (dp[i-1][j] and (s1[i-1] == s3[i+j-1])) or \
        #         (dp[i][j-1] and (s2[j-1] == s3[i+j-1]))
        # return dp[-1][-1]

        # DFS BFS
        # 分别为 s1的第x个字符，s2的第y个字符
        stack, visited = [(0, 0)], set((0,0))
        while stack:
            # DFS
            x, y = stack.pop()
            # BFS
            # x, y = stack.pop(0)
            if x+y == len(s3):
                return True
            if x+1 <= m and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= n and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))
        return False
s=Solution()
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
# @lc code=end

