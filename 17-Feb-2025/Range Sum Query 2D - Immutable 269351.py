# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Create a new matrix for storing prefix sums
        self.psum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        # Fill the prefix sum matrix
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                # Calculate prefix sum as the sum of the current element, left, and top subarrays
                self.psum[i][j] = matrix[i - 1][j - 1] + self.psum[i - 1][j] + self.psum[i][j - 1] - self.psum[i - 1][j - 1]
                
        print(self.psum)  # This is just for debugging; you can remove it later

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the sum of the region by using the inclusion-exclusion principle
        return (self.psum[row2 + 1][col2 + 1]
                - self.psum[row1][col2 + 1]
                - self.psum[row2 + 1][col1]
                + self.psum[row1][col1])

# Example usage:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)
