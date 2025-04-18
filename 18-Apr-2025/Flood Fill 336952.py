# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        oldValue=image[sr][sc]
        visited=set()
        visited.add((sr,sc))
        queue=deque()
        queue.append((sr,sc))
        image[sr][sc]=color
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    
                    if (nr, nc) not in visited and image[nr][nc] == oldValue:
                        image[nr][nc] = color
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        return image

        