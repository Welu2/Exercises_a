# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = []
        v =set(nums)
        for n in v:
            if nums.count(n) > (len(nums) // 3):
                t.append(n)
        return t
        