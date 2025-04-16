# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        rotten=deque()
        n=len(grid)
        m=len(grid[0])
        def inbound(x,y):
            return 0<= x < n and 0<=y<m
        fresh=0
        time=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                u,v = rotten.popleft()
                for d in directions:
                    x=u+d[0]
                    y=v+d[1]
                    if inbound(x,y) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh-=1
                        rotten.append((x,y))
            time+=1

        return time if fresh == 0 else -1
                    

        