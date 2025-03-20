# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
n=int(input())

for _ in range(n):
    t=int(input())
    s=input()
    whole=Counter(s)
    leftOver=Counter()
    maxDistinct=0
    for char in s:
        whole[char]-=1
        leftOver[char]+=1
        if whole[char] == 0:
            del whole[char]
        maxDistinct=max(maxDistinct,(len(whole)+len(leftOver)))

    print(maxDistinct)

    
    