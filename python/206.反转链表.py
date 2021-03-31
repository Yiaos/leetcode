#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ans = tmp = ListNode()
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归
        if not head or not head.next:
            return head
        
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead

        # 循环
        # prev = None
        # curr = head
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
            
        # return prev

# @lc code=end

