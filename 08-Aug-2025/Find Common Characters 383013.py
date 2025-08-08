# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a=words[0]
        k=words[1:]
        pos=[]
        
        for i in a:
            if all(i in j for j in k):
                pos.append(i)


        d=Counter(pos)
        cor=defaultdict(int)
        for t in d:
            for j in words:
                h=Counter(j)
                
                if cor[t] != 0:
                    cor[t]= min(h[t],d[t],cor[t])
                else:
                    cor[t]= min(h[t],d[t])

        ans=[]
        for i in cor:
            for j in range(cor[i]):
                ans.append(i)
        return ans
            