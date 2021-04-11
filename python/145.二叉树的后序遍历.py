#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # def helper(root, ans):
        #     if root:
        #         helper(root.left, ans)
        #         helper(root.right, ans)
        #         ans.append(root.val)
        # ans = []
        # helper(root, ans)
        # return ans

        # 迭代
        if not root:
            return []
        stack = []
        ans = []
        prev_visited = None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            root = stack.pop()
            # 如果右子树存在且未被访问， root重新入栈
            if root.right and root.right != prev_visited:
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                prev_visited = root
                # 终止第一步root遍历
                root = None
# @lc code=end

