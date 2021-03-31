#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 循环遍历 hash
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False

        # 快慢双指针
        # if not head or not head.next:
            # return False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# @lc code=end

