#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # # 二分法-循环
        def getKthElement(k):
            idx1 = idx2 = 0
            while True:
                if idx1 == m:
                    return nums2[k+idx2-1]
                if idx2 == n:
                    return nums1[k+idx1-1]
                if k == 1:
                    return min(nums2[idx2], nums1[idx1])
        
                new_idx1 = min(m-1, idx1 + k // 2 -1)
                new_idx2 = min(n-1, idx2 + k // 2- 1)
                if nums1[new_idx1] < nums2[new_idx2]:
                    k -= new_idx1 - idx1 +1
                    idx1 = new_idx1 +1
                else:
                    k -= new_idx2 -idx2 +1
                    idx2 = new_idx2 + 1
        
        m, n = len(nums1), len(nums2)
        _len = m + n
        if _len % 2 == 0:
            return (getKthElement((_len)//2) + getKthElement((_len//2)+1))/2
        else:
            return getKthElement((_len+1)//2)


        # # 二分法-递归
        # def get_kth(k, l1, l2):
        #     len1 = len(l1)
        #     len2 = len(l2)
        #     if not l1:
        #         return l2[k]
        #     if not l2:
        #         return l1[k]
            
        #     i = len1//2
        #     j = len2//2
        #     if i + j < k:
        #         if l1[i] < l2[j]:
        #             l1=l1[i+1:]
        #             k -= i +1 
        #         else:
        #             l2=l2[j+1:]
        #             k -= j+1
        #         return get_kth(k, l1, l2)
        #     else:
        #         if l1[i] > l2[j]:
        #             l1 = l1[:i]
        #         else:
        #             l2 = l2[:j]
        #         return get_kth(k, l1, l2)
        
        # _len = len(nums1) + len(nums2)
        # if _len % 2 == 1:
        #     return get_kth((_len)//2, nums1, nums2)
        # else:
        #     return (get_kth((_len)//2, nums1, nums2) + get_kth((_len)//2-1, nums1, nums2))/2


        # # 未实现的
        # if len(nums1) > len(nums2):
        #     return self.findMedianSortedArrays(nums2, nums1)

        # infinty = 2**40
        # m, n = len(nums1), len(nums2)
        # left, right = 0, m
        # # median1：前一部分的最大值
        # # median2：后一部分的最小值
        # median1, median2 = 0, 0

        # while left <= right:
        #     # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
        #     # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
        #     i = (left + right) // 2
        #     j = (m + n + 1) // 2 - i

        #     # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
        #     nums_im1 = (-infinty if i == 0 else nums1[i - 1])
        #     nums_i = (infinty if i == m else nums1[i])
        #     nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
        #     nums_j = (infinty if j == n else nums2[j])

        #     if nums_im1 <= nums_j:
        #         median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
        #         left = i + 1
        #     else:
        #         right = i - 1

        # return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1



s =Solution()
print(s.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))

# @lc code=end

