#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            if not node:
                return 0

            # 左右节点最大贡献值
            # 只有在贡献值大于0时，才会选取该节点
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            # 节点的最大路径和取决于该节点的值和左右子节点的最大贡献值
            node_gain = node.val + left_gain + right_gain
            # 更新答案
            self.max_sum = max(self.max_sum, node_gain)
            # 返回节点的最大贡献值
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
# @lc code=end

