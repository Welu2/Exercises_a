# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        k=''
        p=list(map(str,s.split()))
        for i in range(len(p)-1,-1,-1):
            k+=p[i]
            k+= ' '
        
        return k.strip()
        