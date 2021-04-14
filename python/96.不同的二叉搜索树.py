#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划
        # 数字i作为根，则1...i-1为左子树， i+1...n作为右子树
        # 可以分解成多个子问题，且子问题的解可以复用，使用动态规划
        # G(n)表示长度为n的序列能构成的二叉搜索数的数量
        # F(i, n):表示以i为根，序列长度为n的二叉搜索树个数(1<=i<=n)
        # F(i, n) = G(i-1)*G(n-i)
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, n+1):
                G[i] += G[j-1]*G[i-j]
        return G[-1]

        # 卡塔兰数
        C = 1
        for i in range(n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
# @lc code=end

