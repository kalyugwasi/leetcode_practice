#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Medium (58.08%)
# Likes:    5669
# Dislikes: 8546
# Total Accepted:    868.8K
# Total Submissions: 1.5M
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters chars, compress it using the following
# algorithm:
# 
# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
# 
# 
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# 
# 
# The compressed string s should not be returned separately, but instead, be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
# 
# After you are done modifying the input array, return the new length of the
# array.
# 
# You must write an algorithm that uses only constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to
# "a2b2c3".
# 
# 
# Example 2:
# 
# 
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a
# single character.
# 
# 
# Example 3:
# 
# 
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to
# "ab12".
# 
# 
# Constraints:
# 
# 
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or
# symbol.
# 
# 
#

# @lc code=start
class Solution:
    def compress(self, chars: list[str]) -> int:
        write, read = 0, 0
        n = len(chars)
        while read < n:
            char = chars[read]
            cnt = 0
            while read < n and chars[read] == char:
                read += 1
                cnt += 1
            chars[write] = char
            write += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[write] = c
                    write += 1
        return write


sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
# @lc code=end

