# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
t= int(input())
for _ in range(t):
    s=input()
    t=input()
    p=input()
    flag=True
    i=0
    j=0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
    if i != len(s):
        flag=False
    requried=Counter(t)
    available=Counter(s+p)
    for i in requried:
        if requried[i] > available[i]:
            flag=False
            break

    if flag:
        print("YES")
    else:
        print("NO")

