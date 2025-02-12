# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i,char in enumerate(s):
            lastindex[char]=i

        answer=[]
        l=0
        r=0
        for i in range(len(s)):
            r=max(r,lastindex[s[i]])
            if i == r:
                answer.append(r+1-l)
                l=r+1

        return answer
