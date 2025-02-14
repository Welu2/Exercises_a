# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        nums.sort()
        cur=0
        
        mvav=float('inf')
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l < r:
                cur =nums[l]+nums[i]+nums[r]
                if abs(target-cur) < abs(target-mvav):
                    mvav=cur

                if cur < target:
                    l+=1
                elif cur > target:
                    r-=1
                else:
                    return cur

        return mvav