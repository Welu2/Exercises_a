# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = []
        v =set(nums)
        for n in v:
            if nums.count(n) > (len(nums) // 3):
                t.append(n)
        return t
        