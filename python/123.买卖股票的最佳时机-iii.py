#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        buy_two = buy_one = -float('inf')
        sell_two = sell_one = 0
        for p in prices:
            buy_one = max(buy_one, -p)
            sell_one = max(sell_one, buy_one + p)
            buy_two = max(buy_two, sell_one - p)
            sell_two = max(sell_two, buy_two + p)

        return sell_two


s=Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
# @lc code=end

