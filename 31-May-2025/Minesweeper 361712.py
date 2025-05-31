# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board

        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]

        def count_adjacent_mines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                if board[r][c] != 'E':
                    continue
                mines = count_adjacent_mines(r, c)
                if mines == 0:
                    board[r][c] = 'B'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'E':
                            queue.append((nr, nc))
                else:
                    board[r][c] = str(mines)

        click_r, click_c = click
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            bfs(click_r, click_c)

        return board
        