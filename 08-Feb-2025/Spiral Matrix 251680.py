# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer=[]
        top=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        left=0
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                answer.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                answer.append(matrix[j][right])
            right-=1
            if top > bottom or left>right:
                break
            for i in range(right,left-1,-1):
                answer.append(matrix[bottom][i])
            bottom-=1
            for j in range(bottom,top-1,-1):
                answer.append(matrix[j][left])
            left+=1

        return answer
