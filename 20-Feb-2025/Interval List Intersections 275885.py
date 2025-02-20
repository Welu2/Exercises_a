# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        left=0
        right=0
        out=[]
        while left < len(firstList) and right <len(secondList):
            start1,end1=firstList[left]
            start2,end2=secondList[right]
            if start1 <= end2 and start2 <= end1:
                out.append([max(start1,start2),min(end1,end2)])
            if end1 > end2:
                right+=1
            else:
                left+=1

        return out