#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode()
        dummy.next = l = r = head

        while True:
            count = 0
            while count < k and r:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    # reverse
                    cur.next, pre, cur = pre, cur, cur.next
                # connect left and right
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
# @lc code=end

