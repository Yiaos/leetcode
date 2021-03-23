#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        ans = 10**6
        for first in range(len(nums)-2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = len(nums) - 1
            second = first + 1
            while second < third:
                if second > first + 1 and nums[second - 1] == nums[second]:
                    second += 1
                    continue
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return target
                if abs(s - target) < abs(ans-target):
                    ans = s
                if s > target:
                    third -= 1
                else:
                    second += 1
            # for second in (range(first+1, len(nums))):
            #     while second < third:
            #         s = nums[first] + nums[second] + nums[third]
            #         if s == target:
            #             return target
            #         if abs(s - target) < abs(ans-target):
            #             ans = s
            #         if s > target:
            #             third -= 1
            #         else:
            #             break
            #     if second == third:
            #         break
        return ans
s = Solution()
print(s.threeSumClosest(nums = [-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6], target = 18))
# @lc code=end

