# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c= Counter(arr1)
        ans=[]
        for i in arr2:
            if i in c:
                for j in range(c[i]):
                    ans.append(i)
        
        left=[]
        for j in set(arr1):
            if j not in arr2:
                for i in range(c[j]):
                    left.append(j)
        left.sort()
       

        return ans+left
