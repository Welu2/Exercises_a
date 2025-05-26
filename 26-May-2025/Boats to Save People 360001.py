# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        c=0
        while l <= r:
            f=people[l] + people[r]
            if f <= limit:
                
                l+=1
            r-=1
            c+=1

        return c
        