#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. little trick
        # 遍历当和小于0时直接舍弃，和大于0时继续累加
        # 如果全部小于0则取最大值 ans = max(ans, sum)
        # if not nums:
        #     return
        # ans = nums[0]
        # sum = 0
        # for i in nums:
        #     if sum > 0:
        #         sum = sum + i
        #     else:
        #         sum = i
        #     ans = max(ans, sum)
        # return ans

        # 2. 动态规划
        # if not nums:
        #     return
        # ans = nums[0]
        # pre = 0
        # for i in nums:
        #     pre = max(pre + i, i)
        #     ans = max(pre, ans)
        # return ans

        # 3. 分治
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            # 递归分别计算左右最大子序列和
            mid = n // 2
            left = self.maxSubArray(nums[:mid])
            right = self.maxSubArray(nums[mid:])
        # 计算中间的最大子序列和
        # 从左侧最右开始计算左侧最大子序列和
        # 从右侧最左侧开始计算左侧最大子序列和
        # 相加即为中间的最大子序列和
        max_l = nums[n//2-1]
        pre = 0
        for i in range(n//2-1, -1, -1):
            pre += nums[i]
            max_l = max(max_l, pre)
        pre = 0
        max_r = nums[n//2]
        for i in range(n//2, n):
            pre += nums[i]
            max_r = max(max_r, pre)
        return max(max_l+max_r, left, right)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# @lc code=end

