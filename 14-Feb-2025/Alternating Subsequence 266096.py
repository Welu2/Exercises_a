# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    mtoatal=0
    while i < n:
        maxval=arr[i]
        while i +1 < n and (arr[i]*arr[i+1]) > 0:
            maxval=max(maxval,arr[i+1])
            i+=1
        mtoatal+=maxval
        i+=1

    print(mtoatal)


