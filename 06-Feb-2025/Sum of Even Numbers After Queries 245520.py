# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer=[]
        total=sum(j for j in nums if j %2==0)
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 ==0:
                total-=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            if nums[queries[i][1]] % 2 ==0:
                total+=nums[queries[i][1]]

            answer.append(total)

        return answer