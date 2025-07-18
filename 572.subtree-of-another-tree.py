#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.SameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or
                self.isSubtree(root.right,subRoot))
    def SameTree(self,root , subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.SameTree(root.left,subRoot.left) and
                    self.SameTree(root.right,subRoot.right))
        return False
# @lc code=end

