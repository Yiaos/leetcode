#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # O(n^2)
        # def height(root):
        #     if not root:
        #         return 0
        #     return max(height(root.left), height(root.right)) + 1

        # if not root:
        #     return True
        # left = height(root.left)
        # right = height(root.right)
        # if abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        #     return True
        # return False

        # O(n)
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or (abs(left-right) > 1):
                return -1
            else:
                return max(left, right) + 1

        if height(root) >= 0:
            return True
        return False
# @lc code=end

