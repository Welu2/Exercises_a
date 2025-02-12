# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while l <=r:
            if height[l] < height[r]:
                m=max(m,(r-l)*height[l])
                l+=1
            elif height[l] > height[r]:
                 m=max(m,(r-l)*height[r])
                 r-=1
            else:
                m=max(m,(r-l)*height[r])
                l+=1
                r-=1

        return m