# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        row = len(mat)
        col = len(mat[0])
        ri = 0
        ci = 0
        isforward = True
        
        while len(answer) != row * col:
            if isforward:
                # Move diagonally upwards
                while ri >= 0 and ci < col:
                    answer.append(mat[ri][ci])
                    ri -= 1
                    ci += 1
                
                if ci == col:
                    ci -= 1
                    ri += 2
                else:
                    ri += 1
                isforward = False
            else:
                # Move diagonally downwards
                while ci >= 0 and ri < row:
                    answer.append(mat[ri][ci])
                    ri += 1
                    ci -= 1
                
                if ri == row:
                    ri -= 1
                    ci += 2
                else:
                    ci += 1
                isforward = True
        
        return answer
