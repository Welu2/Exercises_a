# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t=int(input())
def pref(arr):
    array=[0]
    value=0
    for i in range(len(arr)):
        array.append(arr[i]+value)
        value+=arr[i]
    return array
for _ in range(t):
    n=int(input())
    arr1=list(map(int,input().split()))
    m=int(input())
    arr2=list(map(int,input().split()))
    
    ar1=pref(arr1)
    ar2=pref(arr2)
  
    maxV=max(ar1)+max(ar2)
 

    print(maxV)