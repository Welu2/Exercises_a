# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=0
    r=1
    c=0
    while r < n:
        if arr[l] > arr[r]:
            l+=2
            r+=2
            c+=1
        else:
            l+=1
            r+=1
    print(c)