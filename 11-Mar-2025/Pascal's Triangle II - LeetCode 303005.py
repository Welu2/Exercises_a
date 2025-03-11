# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def triangle(rowIndex):
            if  rowIndex == 0 or rowIndex == 1:
                return [1]*(rowIndex+1)
            else:
                ans=[1]*(rowIndex+1)
                back=triangle(rowIndex-1)
                for i in range(1,rowIndex):
                    ans[i] = back[i-1]+ back[i]

                return ans

        return triangle(rowIndex)