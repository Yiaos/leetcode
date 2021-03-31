#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#

# @lc code=start
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 1. 动态规划
        # dp[i, 0] 表示以元素A[i]结束，不删元素的最大子数组和
        # dp[i, 1] 表示以元素A[i]结束，删除了一个元素(可能是第i个元素，也可能是之前的元素)的最大子序列和
        # dp[i, 0] = max(dp[i-1, 0] + arr[i], arr[i])
        # dp[i, 1] = max(dp[i-1, 1] + arr[i], dp[i-1, 0])
        # n = len(arr)
        # dp = [[float('-inf')] * 2 for _ in range(n)]
        # res = float('-inf')
        # for i, a in enumerate(arr):
        #     # dp[i-1][0]<0 ture or not
        #     dp[i][0] = max(dp[i-1][0] + a, a)
        #     dp[i][1] = max(dp[i-1][1] + a, dp[i-1][0])
        #     # res = max(res, *dp[i])
        #     res = max(res, dp[i][0], dp[i][1])
        # return res

        # 2. tricks: 
        # forget dp(i-1, 0) and dp(i-1, 1) after we compute dp(i,0) and dp(i,1)
        # 因为自底向上
        x = y = res = float('-inf')
        for a in arr:
            x, y = max(a, x + a), max(x, y + a)
            res = max(res, x, y)
        return res

        # 3. 易理解的
        # left[i]: 为从左向右以i结尾的子序列最大和
        # right[i]: 为从右向做以i结尾的子序列最大和
        # res: 1. 不删除： max(left)   2. 删除left[i-1]+right[i+1]的最大值
        # n = len(arr)
        # left = [float('-inf')] * n
        # right = [float('-inf')] * n
        # left[0] = arr[0]
        # right[-1] = arr[-1]
        # for i in range(1, n):
        #     left[i] = max(left[i-1] + arr[i], arr[i])
        # for i in range(n-2, -1, -1):
        #     right[i] = max(right[i+1] + arr[i], arr[i])
        # res = max(left)
        # for i in range(1, n-1):
        #     res = max(res, left[i-1] + right[i+1])
        # return res

s=Solution()
print(s.maximumSum([1,-2,0,3]))
# @lc code=end

