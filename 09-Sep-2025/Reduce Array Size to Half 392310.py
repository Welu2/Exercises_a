# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq=Counter(arr)
        t=[]
        for j in freq:
            t.append(freq[j])

        t.sort(reverse=True)
        total=0
        c=0
        print(t)
        for i in range(len(t)):
    
            if total >= len(arr)//2 :
                break
            total += t[i]
            c+=1

        return c

        
