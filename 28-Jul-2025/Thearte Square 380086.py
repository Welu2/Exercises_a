# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

n,m,a=map(int,input().split())

w=0
l=0
if (n//a)*a < n:
    w=(n//a)+1
    
else:
    w=(n//a)
if (m//a)*a < m:
    l=(m//a)+1
else:
    l=(m//a)


print(l*w)