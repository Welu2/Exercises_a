# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        b=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while a and temperatures[a[-1]] < temperatures[i]:
                b[a[-1]]=i-a[-1]  
                a.pop()
            a.append(i)

        

        return b

        
