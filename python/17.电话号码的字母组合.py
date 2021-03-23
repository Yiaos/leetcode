#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str):
        da_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        # 1. 回溯
        # if not digits:
        #     return []
        # if len(digits) == 1:
        #     return list(da_map[digits])
        
        # prev = self.letterCombinations(digits[:-1])
        # next = da_map[digits[-1]]

        # return [a+b for a in prev for b in next]

        # 2. 回溯
        # def backtrack(idx):
        #     if idx == len(digits):
        #         ans.append("".join(combin))
        #     else:
        #         digit = digits[idx]
        #         for letter in da_map[digit]:
        #             combin.append(letter)
        #             backtrack(idx+1)
        #             combin.pop()
        # ans = list()
        # combin = list()
        # backtrack(0)
        # return ans

        # 3. oneliner
        # import itertools
        # groups = [da_map[digit] for digit in digits]
        # return ["".join(combin) for combin in itertools.product(*groups)]

        # 3. 队列， 广度优先搜索
        if not digits:
            return []
        import collections
        deque = collections.deque()
        deque.append("")
        for i in range(len(digits)):
            deque_len = len(deque)
            for j in range(deque_len):
                letters = da_map[digits[i]]
                curr_deque = deque.popleft()
                for letter in letters:
                    deque.append(curr_deque+letter)
        return list(deque)

s = Solution()
print(s.letterCombinations("24"))
# @lc code=end

