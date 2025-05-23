# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = []
        result = []
        
        
        for i in range(n + 1):
            stack.append(i + 1)  
            
            
            if i == n or pattern[i] == "I":
    
                while stack:
                    result.append(str(stack.pop()))
        
        
        return "".join(result)
