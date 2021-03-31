#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 循环
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return curr
        #     visited.add(curr)
        #     curr = curr.next
        # return None

        # 快慢指针
        fast = slow = head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None
        
# @lc code=end

