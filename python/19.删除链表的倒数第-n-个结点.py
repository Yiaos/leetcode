#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. 双指针
        # fast = slow = head
        # print(id(fast),id(slow), id(head))
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next
        # slow.next = slow.next.next
        # return head
    
        # 2. 遍历获取长度
        # dummy = ListNode(0, head)
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        # curr = dummy
        # for _ in range(length-n):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return dummy.next

        # 3. value-shifting
        # def index(node):
        #     if not node:
        #         return 0
        #     i = index(node.next) + 1
        #     if i > n:
        #         node.next.val = node.val
        #     return i
        # index(head)
        # return head.next

        # 4. Index and Remove
        def remove(node):
            if not node:
                return 0, node
            i, node.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]
# @lc code=end

