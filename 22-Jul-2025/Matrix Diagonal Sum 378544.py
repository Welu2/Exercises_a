# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        n=len(mat)-1
        for i in range(n+1):
            total += mat[i][i] 
            total += mat[i][n-i]
        
        
        if n%2 ==0:
            return total-mat[n//2][n//2]

        return total
        

