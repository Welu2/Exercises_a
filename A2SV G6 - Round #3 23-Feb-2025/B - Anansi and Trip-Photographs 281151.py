# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    l=0
    r=n
    checker=True
    while r < len(arr):
        if arr[r]-arr[l] < x:
            checker=False
            

        l+=1
        r+=1
    if checker:
        print('YES')
    else:
        print('NO')
        