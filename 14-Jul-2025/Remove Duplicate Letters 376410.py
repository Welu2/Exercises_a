# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        a=Counter(s)
        b=[]
        c=set()
        for i in s:
            a[i] -=1
            if i in c:
                continue
            while b and a[b[-1]] > 0 and b[-1] > i:
                e=b.pop()
                c.remove(e)

            b.append(i)
            c.add(i)
            



        return ''.join(b)