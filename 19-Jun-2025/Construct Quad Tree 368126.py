# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform( grid, row, col, size):
            val = grid[row][col]
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != val:
                        return False
            return True

        def buildTree(row, col, size):
            if isUniform(grid, row, col, size):
                return Node(grid[row][col] == 1, True)

            half = size // 2
            return Node(
                True,  # value doesn't matter for internal nodes
                False,
                buildTree(row, col, half),  # top-left
                buildTree(row, col + half, half),  # top-right
                buildTree(row + half, col, half),  # bottom-left
                buildTree(row + half, col + half, half)  # bottom-right
            )

        return buildTree(0, 0, len(grid))

 