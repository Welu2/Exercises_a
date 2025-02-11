# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            minv=i
            for j in range(i+1,len(arr)):
                if arr[minv] > arr[j]:
                    minv=j
                    
            arr[i],arr[minv] = arr[minv],arr[i]
            
        return arr
                    