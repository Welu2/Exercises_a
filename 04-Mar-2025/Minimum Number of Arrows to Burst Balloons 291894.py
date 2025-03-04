# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        array = sorted(points, key=lambda x: x[1])
        count=0
        end = float('-inf')
        
        for start, balloon_end in array:
            if start > end:
                count += 1
                end = balloon_end 
               
        
        return count
       

