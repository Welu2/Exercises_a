# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=''
        for i in s:
            a+=str(ord(i)-96)
            
        while k>0:
            c=0
            for i in a:
                c+=int(i)

            a=str(c)
            k-=1
        
        return int(a)