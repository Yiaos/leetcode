#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(s, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    result_of_rest = backtrack(s[len(word):], memo)
                    for itm in result_of_rest:
                        itm = word + ' ' + itm
                        res.append(itm)

            memo[s] = res
            return res
    
        memo = {}
        return backtrack(s, memo)

# @lc code=end

