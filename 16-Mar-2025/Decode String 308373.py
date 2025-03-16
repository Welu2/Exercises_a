# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        digit = []  
        output = []  
        sub = []  
        num = 0  
        
        for i in s:
            if i.isdigit():
                
                num = num * 10 + int(i)
            elif i == '[':
           
                digit.append(num)
                num = 0
        
                output.append(''.join(sub))
                sub = []
            elif i == ']':
          
                last_output = output.pop()
                repeat_count = digit.pop()
                sub_str = ''.join(sub)
            
                sub = [last_output + sub_str * repeat_count]
            else:
              
                sub.append(i)

        return ''.join(sub)