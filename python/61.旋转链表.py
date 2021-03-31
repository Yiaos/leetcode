#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length = 1
        # 环
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        curr = head
        k = k % length
        for _ in range(length - 1 - k):
            curr = curr.next
        ans = curr.next
        curr.next = None
        return ans

        
# @lc code=end

