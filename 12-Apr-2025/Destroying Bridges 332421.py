# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if k == 0:
        print(n)
    else:
        for i in range(1,n+1):
            if i*(n-i)<=k:
                print(i)
                break