# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis=[]
        for p in points:
            dis.append([sqrt(p[0]**2 +p[1]**2),p])
       
        dis=sorted(dis,key= lambda x: x[0])
        ans=[]
        for j in range(k):
            ans.append(dis[j][1])
        return ans
