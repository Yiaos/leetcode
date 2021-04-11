#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 交换
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        # 快排
        # def quick_sort(nums, l, r):
        #     if l >= r:
        #         return
        #     left, right = l, r
        #     povit = nums[l]
        #     while l < r:
        #         while l < r and nums[r] <= povit:
        #             r -= 1
        #         while l < r and nums[l] >= povit:
        #             l += 1
        #         if l < r:
        #             swap(nums, r, l)
        #     swap(nums, left, l)
        #     quick_sort(nums, left, l-1)
        #     quick_sort(nums, l+1, right)

        # 快速选择
        # def quick_select(nums, l, r, index):
        #     p = partition(nums, l, r)
        #     if p == index:
        #         return nums[p]
        #     elif p < index:
        #         return quick_select(nums, p+1, r, index)
        #     else:
        #         return quick_select(nums, l, p-1, index)
        
        # def partition(nums, l, r):
        #     p = random.randint(l, r)
        #     swap(nums, l, p)
        #     povit = nums[l]
        #     i, j = l, r
        #     while i < j:
        #         while i < j and nums[j] >= povit:
        #             j -= 1
        #         while i < j and nums[i] <= povit:
        #             i += 1
        #         swap(nums, i, j)
        #     swap(nums, l, i)
        #     return i

        # n = len(nums)
        # return quick_select(nums, 0, len(nums)-1, len(nums)-k)

        # 堆排序
        # def heap_sort(nums):
        #     # 大顶堆
        #     size = len(nums)
        #     for i in range((size-2)//2, -1, -1):
        #         build_heap(nums, i, size)
            
        #     for i in range(size-1, 0, -1):
        #         swap(nums, 0, i)
        #         build_heap(nums, 0, i-1)
                
        def build_heap(nums, root, size):
            child = root * 2 + 1
            if child >= size:
                return
            if child + 1 < size and nums[child+1] > nums[child]:
                child += 1
            if nums[child] > nums[root]:
                swap(nums, child, root)
            
            build_heap(nums, child, size)


        # 堆选择
        def heap_select(nums, k):
            for i in range((n-2)//2, -1, -1):
                build_heap(nums, i, n)
            
            for i in range(1, k):
                swap(nums, 0, n-i)
                build_heap(nums, 0, n-i)

            return nums[0]


        n = len(nums)
        # heap_sort(nums)
        return heap_select(nums, k)


s=Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(s.findKthLargest([3,2,1,5,6,4], 2))
# @lc code=end

