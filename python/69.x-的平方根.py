#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, x
        while l <= r:
            mid = (l+r)//2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

# @lc code=end

