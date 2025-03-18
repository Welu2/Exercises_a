# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def compare(root,val):
            if root == None:
                return TreeNode(val)
            if val > root.val:
                root.right=compare(root.right,val)
            if val < root.val:
                root.left=compare(root.left,val)
            return root

        return compare(root,val)

        