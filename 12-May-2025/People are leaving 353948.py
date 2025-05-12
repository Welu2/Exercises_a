# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

def solve():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    next_alive = list(range(n + 2))  # index 1 to n; n+1 is dummy for bounds

    def find(x):
        if next_alive[x] != x:
            next_alive[x] = find(next_alive[x])
        return next_alive[x]

    index = 2
    result = []

    for _ in range(m):
        op = data[index]
        x = int(data[index + 1])
        index += 2

        if op == '-':
            next_alive[x] = find(x + 1)
        else:  # op == '?'
            res = find(x)
            if res > n:
                result.append("-1")
            else:
                result.append(str(res))

    print("\n".join(result))

solve()