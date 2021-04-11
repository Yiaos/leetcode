#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先+回溯
        def backtrack(i, j, k, visited):
            if word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            ans = False
            for d in direction:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                    if backtrack(new_i, new_j, k+1, visited):
                        ans = True
                        break
            visited.remove((i, j))
            return ans

        direction = [[0,1], [0,-1], [1,0], [-1, 0]]
        m = len(board)
        n = len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0, visited):
                    return True
        return False

s=Solution()
print(s.exist(board = [["a","b"],["c","d"]], word = "acdb"))
        
# @lc code=end

