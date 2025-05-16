# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t=int(input())
for _ in range(t):
    n=int(input())
    p=-n&n
    
    if n == 1:
        print(3)
    elif p==n:
        print(p+1)
    else:
        print(p)
    