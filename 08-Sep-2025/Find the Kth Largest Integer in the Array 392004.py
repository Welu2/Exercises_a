# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        g=[]
        for j in nums:
            g.append(int(j))

        g.sort(reverse=True)

        return str(g[k-1])
