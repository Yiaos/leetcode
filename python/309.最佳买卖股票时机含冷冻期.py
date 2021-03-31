#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] 未持有或卖出
        # dp[i][1] 持有
        # dp[i][2] 冷却期，不买卖
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            # 前一天未持有 或 前一天持有,今天卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 前一天持有 或 前一天未持有，且前一天未卖出（今天不是冷却期）,则两天及之前卖出
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
            # 冷却期:前一天买入
            dp[i][2] = dp[i-1][1]

        return dp[-1][0]

s=Solution()
print(s.maxProfit([1,2,3,0,2]))
# @lc code=end

