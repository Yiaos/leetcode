#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 动态规划
        # # dp[i][j]:楼层  i->步数， j->鸡蛋
        # # 初始化1. no move no floor --> dp[0][*] = 0
        # # 初始化2. no egg no floor  --> dp[*][0] = 0
        # dp = [[0] * (k+1) for _ in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, k+1):
        #         # 1. pick on egg and drop
        #         # 2. have k or k-1 eggs, depending on weather the previous egg broken
        #         # 3. broken: 1+dp[i-1][j-1]  not broken: dp[i-1][j]
        #         dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + 1
        #         if dp[i][j] >= n:
        #             return i
    
        # 递归
        # t-> 扔的次数，

        # 计算能确定碎或不碎的楼层
        def calcfloor(k, t):
            # 只能扔一次或只有一个鸡蛋
            if t == 1 or k == 1:
                return t + 1
            return calcfloor(k-1, t-1) + calcfloor(k, t-1)
        
        t = 1
        while calcfloor(k, t) <= n:
            t += 1
        return t
# @lc code=end

