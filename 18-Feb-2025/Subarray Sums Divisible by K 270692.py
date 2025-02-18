# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cursum=0
        c=0
        d=defaultdict(int)
        d[0]=1
       
        for i in range(len(nums)): 
            cursum+=nums[i]
            r=  cursum % k 
            if r < 0:
                c+=k   
            c+=d[r] 
            d[r]+=1
            
          

        return c
          