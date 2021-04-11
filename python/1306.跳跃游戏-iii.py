#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#

# @lc code=start
from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        if 0 not in arr:
            return False

        n = len(arr)
        dq = deque([start])
        used_set = {start}
        while dq:
            i = dq.popleft()
            v = arr[i]
            for j in [i-v, i+v]:
                if 0 <= j < n and j not in used_set:
                    if arr[j] == 0:
                        return True
                    dq.append(j)
                    used_set.add(j)
        return False

s=Solution()
print(s.canReach(arr = [3,0,2,1,2], start = 2))

# @lc code=end

