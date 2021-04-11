#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list, target: int):
        def findNsum(nums, N, target, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1] * N:
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(len(nums)-N+1):
                    # 重复跳过
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNsum(nums[i+1:], N-1, target - nums[i], result+[nums[i]], results)


        results = []
        nums.sort()
        findNsum(nums, 4, target, [], results)
        return results
        

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
# @lc code=end

