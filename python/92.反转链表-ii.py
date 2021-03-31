#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        # 前面不需要翻转的
        for _ in range(left - 1):
            pre = pre.next
        # 翻转
        reverse = None
        curr = pre.next
        for i in range(left, right+1):
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next
        
        # 连接后续节点
        pre.next.next = curr
        pre.next = reverse
        return dummy.next

h = dummy = ListNode()
for i in range(1,6):
    h.next =  ListNode(i)       
    h = h.next
s=Solution()
res = s.reverseBetween(dummy.next, 2, 4)
# @lc code=end

