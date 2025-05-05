# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(s):
            r = n - 1 - (s - 1) // n
            c = (s - 1) % n if (n - 1 - r) % 2 == 0 else n - 1 - (s - 1) % n
            return r, c

        visited = set()
        queue = deque([(1, 0)])  # (square number, moves)

        while queue:
            s, moves = queue.popleft()
            if s == n * n:
                return moves

            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                r, c = get_coordinates(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        
        return -1