# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        iscomment = False  # Tracks if inside a block comment
        answer = []  # Stores final output lines
        m = []  # Stores characters for the current line
        
        for line in source:
            j = 0  # Reset index for each new line
            
            if not iscomment:
                m = []  # Reset m only if we are not in a block comment
            
            while j < len(line):
                if not iscomment and j + 1 < len(line) and line[j] == "/" and line[j + 1] == "/":
                    break  # Ignore rest of line due to `//` comment
                
                elif not iscomment and j + 1 < len(line) and line[j] == "/" and line[j + 1] == "*":
                    iscomment = True  # Start block comment
                    j += 1  # Skip `*`
                
                elif iscomment and j + 1 < len(line) and line[j] == "*" and line[j + 1] == "/":
                    iscomment = False  # End block comment
                    j += 1  # Skip `/`
                
                elif not iscomment:
                    m.append(line[j])  
                
                j += 1  
            
            if m and not iscomment:
                answer.append("".join(m))  
        
        return answer
