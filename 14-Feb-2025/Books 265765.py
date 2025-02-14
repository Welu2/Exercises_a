# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=map(int,input().split())
arr=list(map(int,input().split()))
l=0
total=0
m=0
for right in range(n):
    total+=arr[right]
    while total > t:
        total-=arr[l]
        l+=1
    if right-l+1 > m:
        m=right-l+1

print(m)