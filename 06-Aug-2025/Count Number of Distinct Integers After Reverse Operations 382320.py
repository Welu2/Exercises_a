# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_array=[]
        for i in nums:
            a=str(i)
            reversed_array.append(int(a[::-1]))

        return len(set(reversed_array+nums))