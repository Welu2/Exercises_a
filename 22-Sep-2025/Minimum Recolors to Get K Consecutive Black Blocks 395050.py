# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minv=float("inf")
        d=defaultdict(int)
        for j in range(k):
            d[blocks[j]]+=1
        
        minv=min(minv,k-d["B"])

        for i in range(len(blocks)-k):
            d[blocks[i]]-=1
            d[blocks[i+k]]+=1
            minv=min(minv,k-d["B"])

        return minv
