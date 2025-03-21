# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n,m = map(int,input().split())
arr=list(map(int,input().split()))
prefix1=[0]*(n)
prefix2=[0]*(n)

for i in range(1,n):
    cursum=0
    if arr[i-1] > arr[i]:
        cursum=arr[i-1] -arr[i]
    prefix1[i]+=prefix1[i-1]+cursum


for i in range(n-2,-1,-1):
    cursum=0
    prefix2[i]=prefix2[i+1]+max(0,arr[i+1]-arr[i])

for _ in range(m):
    l,r  = map(int,input().split())
    l-=1
    r-=1

    if r > l:
        print(prefix1[r]-prefix1[l])

    else:
            
            print(prefix2[(r)]- prefix2[l])
    
    