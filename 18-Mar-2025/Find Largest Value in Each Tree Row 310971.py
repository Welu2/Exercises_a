# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])  
      
        while queue:
            level_size = len(queue)
            level_max = float('-inf')  

            for _ in range(level_size):
                node = queue.popleft()
                level_max = max(level_max, node.val)
               
                if node.left:
                    queue.append(node.left)
                 
                if node.right:
                    queue.append(node.right)
                    

            result.append(level_max)

        return result



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         def large(root.left, root.right):
#             a=[root.val]
#             if root is None:
#                 return None
#             if root.left and root.right:
#                 a.append(max(root.left.val,root.right.val))
#                 x=root.left
#                 y=root.right
#                 return large(x.left,y.right)
#             elif root.left:
#                 a.append(root.left.val)
#                 return large(x.left,y.right)
#             elif root.right:
#                 a.append(root.right.val)
#                 return large(x.left,y.right)

#             return a
#         return large(root.left,root.right)