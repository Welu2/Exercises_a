# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        maxp=0
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(new_x,new_y):
            return 0 <= new_x < n and 0 <= new_y < m
        
        def dfs(grid,x,y,total):
            nonlocal visited
            if (x,y) in visited:
                return 0
            visited.add((x,y))
            
            total= 1
            for d in directions:
                new_x=x+d[0]
                new_y=y+d[1]
                
                if inbound(new_x,new_y):
                    if grid[new_x][new_y] != 0:
                        total+= dfs(grid,new_x,new_y,total)
                    else:
                        continue
                    
                  
              
            return total
        for j in range(n):
            for i in range(m):
                if (j,i) not in visited and grid[j][i] != 0:
                    maxp=max(maxp,dfs(grid,j,i,0))
        return maxp
        