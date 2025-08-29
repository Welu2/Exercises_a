# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

n=int(input())
i=0
j=0
k=0
for _ in range(n):
    a,b,c =map(int,input().split())
    i+=a
    j+=b
    k+=c
if i == 0 and j == 0 and k == 0:
    print("YES")
else:
    print("NO")