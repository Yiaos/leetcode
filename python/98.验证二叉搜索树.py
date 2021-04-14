#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if root is None:
                return True

            if root.val <= lower or root.val >= upper:
                return False
            if not helper(root.left, lower, root.val):
                return False
            if not helper(root.right, root.val, upper):
                return False
            return True
        
        return helper(root)

        # 遍历， 应为递增数组
        # def inorder(root, lst):
        #     if not root:
        #         return
        #     inorder(root.left, lst)
        #     lst.append(root.val)
        #     inorder(root.right, lst)

        # lst = []
        # inorder(root, lst)
        # for i in range(1, len(lst)):
        #     if lst[i] <= lst[i-1]:
        #         return False
        # return True

# @lc code=end

