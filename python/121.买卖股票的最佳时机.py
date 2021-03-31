#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # max_profit = 0
        # min_price = float('inf')
        # for p in prices:
        #     min_price = min(min_price, p)
        #     max_profit = max(max_profit, p - min_price)
        # return max_profit

        # 动态规划
        # dp[i][0] 卖出或未持有 
        # dp[i][1] 买入或前一天持有
        # 因只买入一次所以卖出时不考虑之前收入
        # 即 dp[i][1]=max(-prices[i], dp[i-1][1])
        # dp = [[0] * 2 for _ in range(len(prices))]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     dp[i][1] = max(-prices[i], dp[i-1][1])
        # return dp[-1][0]

        # O(1) space
        buy, sell = -float('inf'), 0
        for p in prices:
            buy = max(buy, -p)
            sell = max(buy+p, sell)
        return sell

s=Solution()
s.maxProfit([7,1,5,3,6,4])
# @lc code=end

