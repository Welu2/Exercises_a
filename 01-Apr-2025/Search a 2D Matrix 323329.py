# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        val=0
        while l <= r:
            mid=(l+r)//2
            if matrix[mid][0] > target:
                r=mid-1
            if matrix[mid][-1] < target:
                l=mid+1
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                val=mid
                break
        
        l=0
        r=len(matrix[val])-1
        while l <= r :
            mid=(l+r)//2
            if matrix[val][mid] == target:
                return True

            if matrix[val][mid] < target:
                l=mid+1
            else:
                r=mid-1
            

        return False

            
