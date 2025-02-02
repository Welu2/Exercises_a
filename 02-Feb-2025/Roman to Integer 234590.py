# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        l=0
        c=0
        a=['I' ,'V','X','L' ,'C','D' ,'M']
        b=[1,5,10,50,100,500,1000]
        d=dict(zip(a,b))
        while l< len(s):
            if l + 1 < len(s) and d[s[l]] < d[s[l + 1]]: 
                c += d[s[l + 1]] - d[s[l]] 
                l += 2
            else:
                c+=d[s[l]]
                l+=1


        return c
