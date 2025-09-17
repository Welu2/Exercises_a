# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)
        
        
        if len(minutes) > len(set(minutes)):
            return 0

       
        minutes.sort()

        
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        
        wrap_around_diff = 1440 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, wrap_around_diff)

        return min_diff