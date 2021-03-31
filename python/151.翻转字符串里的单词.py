#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.strip().split()[::-1])
        l, r = 0, len(s)-1
        while l <= r and s[l] == ' ':
            l += 1
        while l <= r  and s[r] == ' ':
            r -= 1
        from collections import deque
        dq, words = deque(), []
        while l <= r:
            if s[l] != ' ':
                words.append(s[l])
            elif s[l] == ' ' and words:
                dq.appendleft(''.join(words))
                words = []
            l += 1
        dq.appendleft(''.join(words))
        return ' '.join(dq)
            
            
# @lc code=end

