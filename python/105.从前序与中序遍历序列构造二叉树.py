#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            inorder_root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[inorder_root_index])
            left_child = self.buildTree(preorder, inorder[:inorder_root_index])
            right_child = self.buildTree(preorder, inorder[inorder_root_index+1:])
            root.left = left_child
            root.right = right_child

            return root
# @lc code=end

