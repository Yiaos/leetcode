#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # DFS
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # min_depth = float('inf')
        # if root.left:
        #     min_depth = min(self.minDepth(root.left), min_depth)
        #     print(min_depth)
        # if root.right:
        #     min_depth = min(self.minDepth(root.right), min_depth)
        #     print(min_depth)
        # return min_depth + 1
        
        # BFS 最先到None节点的即为最小高度
        if not root:
            return 0
        from collections import deque
        dq = deque([(root, 1)])
        while dq:
            node, level = dq.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    dq.append((node.left, level+1))
                    dq.append((node.right, level+1))
# @lc code=end

