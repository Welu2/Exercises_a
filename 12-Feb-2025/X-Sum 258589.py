# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def solve():
    t = int(input())  # number of test cases
    
    for _ in range(t):
        # Read the dimensions of the board
        n, m = map(int, input().split())
        
        # Read the board values
        board = [list(map(int, input().split())) for _ in range(n)]
        
        # Precompute the sums for the diagonals
        main_diagonal = {}
        anti_diagonal = {}
        
        # Compute the sums for the diagonals
        for i in range(n):
            for j in range(m):
                main_diag_key = i - j
                anti_diag_key = i + j
                
                if main_diag_key not in main_diagonal:
                    main_diagonal[main_diag_key] = 0
                if anti_diag_key not in anti_diagonal:
                    anti_diagonal[anti_diag_key] = 0
                
                main_diagonal[main_diag_key] += board[i][j]
                anti_diagonal[anti_diag_key] += board[i][j]
        
        # Now calculate the maximal sum for any bishop placement
        max_sum = 0
        
        for i in range(n):
            for j in range(m):
                # Calculate the sum of cells attacked by placing the bishop at (i, j)
                total_sum = main_diagonal[i - j] + anti_diagonal[i + j] - board[i][j]
                max_sum = max(max_sum, total_sum)
        
        # Output the maximum sum for this test case
        print(max_sum)
solve()

