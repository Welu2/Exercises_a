# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        c=0
        a=[]
        for i in s:
            if a and a[-1] == "(" and i ==")":
                a.pop()
            else:
                a.append(i)

        for i in a:
            if i =="(":
                c+=1
            else:
                o+=1

        return c+o
           
