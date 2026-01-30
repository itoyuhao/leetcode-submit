# https://leetcode.com/problems/closest-binary-search-tree-value/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val
        
        while root:  # stop condition: no leaf exist
            if abs(root.val - target) < abs(closest - target):  # do the comparsion before traversing down
                closest = root.val
            
            if abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)
                
            if root.val > target:  # if target is smaller than the node value
                root = root.left

            elif root.val < target:  # if target is bigger than the node value
                root = root.right

            else:
                return closest
        
        return closest
                    