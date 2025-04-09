# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def closer(home):
            l=0
            h=len(heaters)-1
            while l < h:
                mid=(l+h)//2  
                if heaters[mid] > home:
                    h=mid
                else:
                    l=mid+1
           
            minV = abs(heaters[l] - home)
         
            if l > 0:
                minV=min(minV,abs(heaters[l-1]-home))
            return minV
            

        radius=0
        for h in houses:
            radius=max(radius,closer(h))

        return radius