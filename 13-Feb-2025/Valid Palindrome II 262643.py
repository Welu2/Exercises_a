# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        l_mismatched=0
        r_mismatched=0
        if s == s[::-1]:
            return True
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                l_mismatched=left
                r_mismatched=right
                break

        return (s[:l_mismatched]+s[l_mismatched+1:]) ==((s[:l_mismatched]+s[l_mismatched+1:])[::-1]) or ((s[:r_mismatched]+s[r_mismatched+1:])) == ((s[:r_mismatched]+s[r_mismatched+1:])[::-1])