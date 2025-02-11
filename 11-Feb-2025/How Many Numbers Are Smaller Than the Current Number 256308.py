# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        b = nums.copy()
        b.sort()
        l=1
        e=0
        d=[0]
        while l <len(b):
            if b[l] > b[l-1]:
                e+=1
                if l > e:
                    e+=(l-e)
                d.append(e)
            else:
                d.append(e)
            
            l+=1
        z=dict(zip(b,d))
        c= []
        for i in nums:
            c.append(z[i])

      

        return c
        