#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            if not l1 or not l2:
                return l1 or l2
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1 or l2:
                curr.next = l1 or l2
            return dummy.next
        # # 1. 按顺序合并
        # # ans = None
        # # for i in range(len(lists)):
        # #     ans = merge(ans, lists[i])
        # # return ans
        # # 2. 分治合并
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        ans = merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
        return ans

        # 3. 小顶堆, 无法通过
        # 维护一个小顶堆，将所有链表的第一个节点加入小顶堆
        # 每次从小顶堆中弹出一个node加入ans,并将node.next加入小顶堆
        # import heapq
        # if not lists:
        #     return None
        # dummy = ListNode()
        # heap = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(heap, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # curr = dummy
        # while heap:
        #     val, idx = heapq.heappop(heap)
        #     curr.next = ListNode(val)
        #     curr = curr.next
        #     if lists[idx]:
        #         heapq.heappush(heap, (lists[idx].val, idx))
        #         lists[idx] = lists[idx].next
        # return dummy.next

# @lc code=end

