# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d=defaultdict(int)
        #(a+b)%k= ((a%k)+(b%k)%k)
        for x in arr:
            d[((x%k)+k)%k]+=1
        flag=True
        for i in range(0,k):
            if i ==0 or (i ==k//2 and k %2 ==0):
                if d[i] %2 != 0:
                    return False
            elif d[i]!=d[k-i]:
                return False
        return flag
