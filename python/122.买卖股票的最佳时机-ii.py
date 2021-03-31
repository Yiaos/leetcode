#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # dp[i][0] 卖出或未持有 
        # dp[i][1] 买入或前一天持有
        # ans = 0
        # dp = [[0] * 2 for _ in range(len(prices))]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            
        # return dp[-1][0]

        # O(1) space 
        # cur_hold = pre_hold = -float('inf')
        # cur_not_hold = pre_not_hold = 0
        # for p in prices:
        #     pre_hold = cur_hold
        #     pre_not_hold = cur_not_hold
        #     cur_hold = max(pre_hold, pre_not_hold - p)
        #     cur_not_hold = max(pre_not_hold, pre_hold + p)
        # return cur_not_hold if prices else 0           
    
        # 贪心
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                ans += prices[i] - prices[i-1]
        return ans

# @lc code=end

