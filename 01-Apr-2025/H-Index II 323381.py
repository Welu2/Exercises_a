# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        h=len(citations)-1
       
        while l <= h:
            mid = (l+h)//2
            if len(citations)- mid <=citations[mid]:    
                h=mid-1
            else:
            
                l=mid+1
        return len(citations)-l
