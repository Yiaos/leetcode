#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        def check(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)
        
        if not root:
            return True
        return check(root.left, root.right)

        # 迭代
        # from collections import deque
        # def check(l, r):
        #     dq = deque()
        #     dq.append(l)
        #     dq.append(r)
        #     while dq:
        #         l = dq.popleft()
        #         r = dq.popleft()
        #         if not l and not r:
        #             continue
        #         if (not l or not r) or (l.val != r.val):
        #             return False
        #         dq.append(l.right)
        #         dq.append(r.left)
        #         dq.append(l.left)
        #         dq.append(r.right)
        #     return True
        # return check(root.left, root.right)
# @lc code=end

