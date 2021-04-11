#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge = []
        for interval in intervals:
            if merge and merge[-1][1] >= interval[0]:
                merge[-1][1] = max(merge[-1][1], interval[1])
            else:
                merge.append(interval)
        return merge

# @lc code=end

