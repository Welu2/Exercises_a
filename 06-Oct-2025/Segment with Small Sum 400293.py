# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,m = map(int,input().split())
arr=list(map(int,input().split()))

total=0
c=0
l=0
r=0
while r < len(arr):
    total+=arr[r]
    if total <= m:
        c=max(c,r-l+1)
    elif total > m:
        
        total-=arr[l]
        l+=1
    
        
    r+=1

print(c)

