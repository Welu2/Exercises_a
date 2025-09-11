# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        def check(arr):
            arr.sort()
            a=arr[1]-arr[0]
            for i in range(2,len(arr)):
                if arr[i]-arr[i-1] != a:
                    return False

            return True

        for i in range(len(l)):
            ans.append(check(nums[l[i]:r[i]+1]))

        return ans