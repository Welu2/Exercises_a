# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a=indices.copy()
        a.sort()
        d= dict(zip(indices,s))
        r=''
        for i in a:
            r+=d[i]

        return r