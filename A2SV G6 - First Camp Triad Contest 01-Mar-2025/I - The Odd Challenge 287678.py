# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
 
    for i in range(1,n):
        arr[i] += arr[i-1]
 
    for _ in range(q):
        l,r,m = map(int,input().split())
        special =( r -l + 1) * m
 
       
        if l ==1:
             t=arr[n-1] -arr[r-1] + special
        else:
            t = arr[l - 2] + arr[n-1] -arr[r-1] + special
 
             
 
        if t % 2 != 0:
            print("YES")
        else:
            print('NO')
 