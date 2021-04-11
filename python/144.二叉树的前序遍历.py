#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # def helper(root, ans):
        #     if root:
        #         ans.append(root.val)
        #         helper(root.left, ans)
        #         helper(root.right, ans)
        # ans = []
        # helper(root, ans)
        # return ans

        # 迭代， 深度优先
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
# @lc code=end

