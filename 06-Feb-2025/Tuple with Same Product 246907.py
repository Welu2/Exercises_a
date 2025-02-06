# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d[nums[i]*nums[j]].append([nums[i],nums[j]])
        count=0
        def combination(n):
            total=0
            for i in range(1,n):
                total+=i
                
            return total
       
        for key in d:
            if len(d[key])>1:
                count+=combination(len(d[key]))*8
        return count
