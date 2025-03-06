# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i == '#' and a:
                a.pop()
            elif i == '#' and len(a) ==0:
                continue
            else:
                a.append(i)

        for i in t:
            if i == '#' and b:
                b.pop()
            elif  i == '#' and len(b) ==0:
               continue
            else:
                b.append(i)


        return a==b