# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    apos=Counter(arr)
    possible=list(apos.values())
    possible.sort()
    minV=float("inf")
    for i in range(len(possible)):
        curmin=n-(len(possible)-i)*possible[i]

        minV=min(minV,curmin)

    print(minV)