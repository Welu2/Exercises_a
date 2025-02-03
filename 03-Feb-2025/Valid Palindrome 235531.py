# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def remove_non_alphanumeric(s):
            return re.sub(r'[^a-zA-Z0-9]', '', s) #remove char if it is not letter
        s = remove_non_alphanumeric(s)
        left = 0 
        right = len(s) - 1
        while left <= right:
            if (s[left]).lower() == (s[right]).lower():
                left += 1
                right -= 1
           
            else:
                return False
                    
            
            
        return True