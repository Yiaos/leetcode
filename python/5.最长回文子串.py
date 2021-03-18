#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
    # 中心扩散
        max_string = ""
        for i in range(len(s)):
            res = self.max_strng(s, i, i+1)
            if len(max_string) < len(res):
                max_string = res

            res = self.max_strng(s, i-1, i+1)
            if len(max_string) < len(res):
                max_string = res

        return max_string

    def max_strng(self, s, left, right):
        while left >= 0 and right < len(s) and s[right] == s[left]:
            left -= 1
            right += 1
        return s[left+1:right]

    # # 动态规划
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     dp = [[False]*n for _ in range(n)]
    #     ans = ""
    #     for m in range(n):
    #         for i in range(1,n):
    #             j = m + i
    #             if j >= len(s):
    #                 break
    #             if m == 0:
    #                 dp[i][j] = True
    #             elif m == 1:
    #                 dp[i][j] = (s[i] == s[j])
    #             else:
    #                 dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
    #             if dp[i][j] and m +1> len(ans):
    #                 ans = s[i: j+1]

    #     return ans

s = Solution()
print(s.longestPalindrome("glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt"))
# @lc code=end

