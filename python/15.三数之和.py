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
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            i, j = first+1, n-1
            while i < j:
                s = nums[i] + nums[j] + nums[first]
                if s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    ans.append([nums[first], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
        return ans

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end

