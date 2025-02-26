# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
t=int(input())
for _ in range(t):
    n,k,d=map(int,input().split())
    c=float("inf")
    arr=list(map(int,input().split()))
    counter={}
    for j in range(d):
        counter[arr[j]]=counter.get(arr[j],0)+1
    
    c=min(c,len(counter))
    for i in range(1,n-d+1):
        
        counter[arr[i-1+d]]=counter.get(arr[i-1+d],0)+1
        counter[arr[i-1]]-=1
        if counter[arr[i-1]]== 0:
            del counter[arr[i-1]]
        
        c=min(c,len(counter))
    print(c)