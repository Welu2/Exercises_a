# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        c=1
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m) == False:
                l=m+1
            elif isBadVersion(m)==True:
                c=m
                r=m-1

        return c