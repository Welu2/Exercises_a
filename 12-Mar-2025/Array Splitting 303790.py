# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C


n,k = map(int,input().split())
arr=list(map(int,input().split()))
if n==k :
    print(0)
else:
    gaps = []
    for i in range(1, n):
        gaps.append(arr[i] - arr[i - 1])
    
    gaps.sort(reverse=True)
      
        
    total_cost = arr[-1] - arr[0]
   
    
    print(total_cost - sum(gaps[:k-1]))
