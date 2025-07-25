#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        l , r = 0 ,1
        while r < len(prices):
            if prices[r] < prices[l]:
                l += 1
            else:
                profit = max(profit ,prices[r] - prices[l])
                r += 1
        return profit
# @lc code=end

