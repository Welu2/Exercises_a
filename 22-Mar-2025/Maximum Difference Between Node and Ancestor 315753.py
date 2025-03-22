# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, min_value, max_value):
       
            if node is None:
                return
          
  
            nonlocal max_difference
            current_diff = max(abs(min_value - node.val), abs(max_value - node.val))
            max_difference = max(max_difference, current_diff)

        
            new_min = min(min_value, node.val)
            new_max = max(max_value, node.val)

            
            dfs(node.left, new_min, new_max)
            dfs(node.right, new_min, new_max)

      
        max_difference = 0

      
        dfs(root, root.val, root.val)
        return max_difference

        