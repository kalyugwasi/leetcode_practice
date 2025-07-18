#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res , l = 0 , 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf , count[s[r]])
            while (r-l+1) - maxf >k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
        
# @lc code=end

