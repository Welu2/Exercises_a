# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        leftover=0
        pairs=0
        for i in freq:
            pairs+=freq[i]//2
            if freq[i]%2 !=0:
                leftover+=1
        return [pairs,leftover]