# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n=int(input())
arr=list(map(int,input().split()))
questions=int(input())
values=arr.copy()

def prefixsum(arr):
    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]
    return arr
unSorted=prefixsum(values)

arr.sort()
arranged=prefixsum(arr)

for _ in range(questions):
    type,start,end=map(int,input().split())
    if type == 1:
        if start==1:
            print(unSorted[end-1])
        else:
           print(unSorted[end-1]-unSorted[start-2]) 
    else:
        if start==1:
            print(arranged[end-1])
        else:
            print(arranged[end-1]-arranged[start-2])

