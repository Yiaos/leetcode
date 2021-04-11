#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 排序
        tmp = dict()
        for s in strs:
            _s = "".join(sorted(s))
            if _s in tmp:
                tmp[_s].append(s)
            else:
                tmp[_s] = [s,]
        return list(tmp.values())
s=Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# @lc code=end

