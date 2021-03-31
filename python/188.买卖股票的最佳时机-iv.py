#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 动态规划
        # n = len(prices)
        # if n < 2:
        #     return 0
        # k = min(k, n//2)
        # dp = [[[0] * 2] * (k+1) for _ in range(n)]
        # for j in range(k+1):
        #     dp[0][j][1] = -prices[0]
        # for i in range(1, n):
        #     for j in range(1, k+1):
        #         dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
        #         dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        # return dp[-1][-1][0]


        # buy[i][j]表示对prices[0..i]中的价格，进行加好j笔交易，并且持有股票 的最大利润
        # sell[i][j]表示恰好进行j笔交易，并且不持有股票 的最大利润
        n = len(prices)
        if n < 2:
            return 0
        k = min(k, n//2)
        buy = [[-float('inf')] * (k+1) for _ in range(n)]
        sell = [[0] * (k+1) for _ in range(n)]
        buy[0][0] = -prices[0]
        for i in range(1, n):
            buy[i][0] = max(buy[i-1][0], sell[i-1][0] - prices[i])
            for j in  range(1, k+1):
                # 第i-1持有股票 或 
                # 第i天不持有股票对应状态为sell[i-1][j],第i天买入,扣除prices[i]
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                # 第i-1天不持有股票
                # 第i天持有股票 对应状态buy[i-1][j-1], 卖出 加上prices[i]
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])
        # 最大利润为sell[n-1][0...k]中的最大值
        return max(sell[-1])


s=Solution()
print(s.maxProfit(k=2, prices=[3,3,5,0,0,3,1,4]))
# print(s.maxProfit(k=2, prices=[1,2,4]))
# @lc code=end
