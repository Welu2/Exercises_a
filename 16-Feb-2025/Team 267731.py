# Problem: Team - https://codeforces.com/contest/231/problem/A

n=int(input())
 
c=0
for _ in range(n):
    arr=list(map(int,input().split()))
    
    k=0
    for i in arr:
        if i == 1:
            k+=1
    if k >=2:
        c+=1
 
print(c)