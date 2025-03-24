# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0  # Initialize count

        def subtree_sum_and_count(node):
            if not node:
                return (0, 0)  # Base case: sum = 0, count = 0
            
            left_sum, left_count = subtree_sum_and_count(node.left)
            right_sum, right_count = subtree_sum_and_count(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Check if the node's value equals the average of its subtree
            if node.val == total_sum // total_count:
                self.count += 1

            return (total_sum, total_count)

        subtree_sum_and_count(root)
        return self.count

            
        