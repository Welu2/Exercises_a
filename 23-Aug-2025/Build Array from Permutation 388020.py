# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(nums[i])

        return ans