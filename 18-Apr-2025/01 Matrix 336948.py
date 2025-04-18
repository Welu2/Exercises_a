# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       
        m=len(mat)
        n=len(mat[0])
        q=deque()
        d=[[float("inf")]*n for _ in range(m)]  
       
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    d[i][j]=0
                    q.append((i,j))

        directions=[[0,1],[1,0],[-1,0],[0,-1]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    
                    if d[nr][nc] > d[r][c] + 1:
                        d[nr][nc] = d[r][c] + 1
                        q.append((nr, nc))

        return d