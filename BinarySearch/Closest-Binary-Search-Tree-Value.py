1# https://leetcode.com/problems/closest-binary-search-tree-value/description/
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
10
11        closest = root.val
12        
13        while root:  # stop condition: no leaf exist
14            if abs(root.val - target) < abs(closest - target):  # do the comparsion before traversing down
15                closest = root.val
16            
17            if abs(root.val - target) == abs(closest - target):
18                closest = min(closest, root.val)
19                
20            if root.val > target:  # if target is smaller than the node value
21                root = root.left
22
23            elif root.val < target:  # if target is bigger than the node value
24                root = root.right
25
26            else:
27                return closest
28        
29        return closest
30                    