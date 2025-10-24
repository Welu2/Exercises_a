# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n,m=map(int,input().split())
if m > n:
    print(-1)
else:
    minv=0
    if n%m == 0:
        minv=n//2
    else:
        minv=(n//2)+(n%2)
    ans=0
    for i in range(minv,n+1):
        if i %m == 0:
            ans=i
            break

    print(ans)
 