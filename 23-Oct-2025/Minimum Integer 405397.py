# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

q=int(input())
for _ in range(q):
    l,r,d=map(int,input().split())
    if l > d :
        print(d)
    else:
        print(((r//d)+1)*d)