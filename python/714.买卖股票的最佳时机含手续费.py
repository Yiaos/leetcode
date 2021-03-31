#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0] 未持有
        # dp[i][1] 持有
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        # return dp[-1][0]

        # 动态规划 贪心
        # n = len(prices)
        # buy, sell = -prices[0], 0
        # for i in range(1, n):
        #     buy = max(buy, sell - prices[i])
        #     sell = max(sell, buy + prices[i] - fee)
        # return sell

        # 贪心: 易理解 双99%
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit


s=Solution()
print(s.maxProfit([1,3,2,8,4,9], 2))
# @lc code=end

