# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
       
        total=sum(nums)
        a=[total]
        le=0
        for i in nums:
            if i == 0:
                le+=1
                a.append(le+total)
            elif i == 1:
                total-=1
                a.append(le+total)
        print(a)
        maxV=max(a)
        ans=[]
        for i in range(len(nums)+1):
            if a[i]==maxV:
                ans.append(i)

        return ans


        