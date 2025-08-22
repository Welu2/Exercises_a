# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        a=[]
        for i in candies:
            if i+extraCandies >= m:
                a.append(True)
            else:
                a.append(False)

        
        return a