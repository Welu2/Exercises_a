# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prf=[0]*len(arr)
        prf[0]=arr[0]
        for i in range(1,len(arr)):
            prf[i]=prf[i-1]^arr[i]

        ans=[0]*(len(queries))
        
        for i in range(len(queries)):
            u,v=queries[i]
            if u == 0:
                ans[i]=prf[v]
            else:
                ans[i]=prf[u-1]^prf[v]


        
        return ans