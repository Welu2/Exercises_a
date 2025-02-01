# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t=int(input())
for _ in range(t):
    lst=list(map(int,input().split()))
    lst.sort()
    if lst[2] ==lst[0]+lst[1]:
        print("YES")
    else:
        print("NO")