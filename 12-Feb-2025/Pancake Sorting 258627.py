# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ks=[]
        def flip(end):
            start=0
            while start <end:
                arr[start],arr[end] = arr[end],arr[start]
                start+=1
                end-=1
        for i in range(len(arr)-1,-1,-1):
            mv=i
            for j in range(i,-1,-1):
                if arr[j] > arr[mv]:
                    mv=j
            if mv !=i:
                flip(mv)
                flip(i)
                ks.append(mv+1)
                ks.append(i+1)

        return ks
        
        