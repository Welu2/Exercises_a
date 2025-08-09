# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1
        for i in range(n - 1, -1, -1):
            arr[i], max_right = max_right, max(max_right, arr[i])
        return arr
        # ans=[]
        # for i in range(len(arr)):
        #     if i != len(arr)-1:
        #         ans.append(max(arr[i+1:]))
        #     else:
        #         ans.append(-1)

        # return ans