# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        string = [str(i) for i in nums]
        
        if nums[0] == 0:
            return "0"
        
        def compare(string,i,j):
            if int(string[i]+string[j]) <int(string[j]+string[i]):
                return True
            return False

        l=0
        
        for i in range(len(string)):
              
            for j in range(i+1,len(string)):
                if int(string[i][l]) < int(string[j][l]):
                     string[i],string[j]=string[j],string[i]
                elif int(string[i][l]) ==int(string[j][l]):
                    if compare(string,i,j):
                        string[i],string[j]=string[j],string[i]

        return "".join(string)


                    
  