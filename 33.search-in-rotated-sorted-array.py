#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        res = 0
        while l <= r:
            m =(l+r)//2
            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: r=m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m + 1       
        return -1
        
# @lc code=end

