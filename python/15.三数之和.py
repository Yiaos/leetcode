#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        # 双指针
        # 因为不能结果不重复，先排序，重复数值，直接跳过
        # 内层循环，因为已经排序， 左指针游艺， 右指针左移，直至重合
        # 时间复杂度： O(N2), 空间复杂度： O(logN)
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            k = n - 1
            hashmap = {}
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans

s = Solution()
print(s.threeSum([0,0,0]))
# @lc code=end

