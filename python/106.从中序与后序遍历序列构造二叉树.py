#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        right_child = self.buildTree(inorder[root_index+1:], postorder)
        left_child = self.buildTree(inorder[:root_index], postorder)
        root.left = left_child
        root.right = right_child
        return root

# s=Solution()
# print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]))
# @lc code=end

