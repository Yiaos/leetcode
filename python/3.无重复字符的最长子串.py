#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxLen = 0
        # for i in range(1, len(s)+1):
        #     subString = s[i-1:i]
        #     subLen = len(subString)
        #     for x in s[i:]:
        #         if x in subString:
        #             i += 1
        #             break
        #         subString += x
        #     if len(subString) > maxLen:
        #         maxLen = len(subString)
        # return maxLen

        # 滑动窗口
        # maxLength, left, curLength = 0, 0, 0
        # subset = set()
        # if not s:
        #     return 0
        # for i in range(len(s)):
        #     curLength += 1
        #     while s[i] in subset:
        #         subset.remove(s[left])
        #         left += 1
        #         curLength -= 1
        #     subset.add(s[i])
        #     if curLength > maxLength:
        #         maxLength = curLength
        # return maxLength
        
        # 滑动窗口+hash
        maxLength = start = 0
        used_char = {}
        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            used_char[s[i]] = i
        return maxLength



# @lc code=end

