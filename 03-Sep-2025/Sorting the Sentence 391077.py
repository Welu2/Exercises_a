# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split()
        b=[]
        for i in range(len(a)):
            b.append([int(a[i][-1]),a[i][:-1]])

        b.sort()
        c=b[0][1]
        for i in range(1,len(b)):
            c += ' ' +b[i][1]


        return c