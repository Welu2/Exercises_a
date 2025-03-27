# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        def check(mid):
            balls=1
            lastp=position[0]
            for i in range(1,len(position)):
                if position[i]- lastp >= mid:
                    balls+=1
                    lastp=position[i]
                if balls==m:
                    return True
            return False

        low=1
        high=position[-1]- position[0]
        value=0
        while low <= high:
            mid=(low+high)//2
            if check(mid):
                value=mid
                low=mid+1
            else:
                high=mid-1


        return value

        