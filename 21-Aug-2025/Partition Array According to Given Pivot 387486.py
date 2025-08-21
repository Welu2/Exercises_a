# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans=[]
        for i in nums:
            if i < pivot:
                ans.append(i)

        for _ in range(nums.count(pivot)):
      
                ans.append(pivot)
        
        for i in nums:
            if i > pivot:
                ans.append(i)

        return ans
