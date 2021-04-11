#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # def helper(root, ans):
        #     if not root:
        #         return 
        #     helper(root.left, ans)
        #     ans.append(root.val)
        #     helper(root.right, ans)
    
        # ans = []
        # helper(root, ans)
        # return ans
        
        ans = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right
# @lc code=end

