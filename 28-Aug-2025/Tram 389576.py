# Problem: Tram - https://codeforces.com/problemset/problem/116/A

n=int(input())
maxV=0
cursum=0
for _ in range(n):
    a,b = map(int,input().split())
    cursum+=b-a
   
    maxV=max(maxV,cursum)
 
print(maxV)