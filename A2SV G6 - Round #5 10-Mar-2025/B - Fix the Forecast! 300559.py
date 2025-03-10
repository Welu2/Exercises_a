# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr1=list( map(int,input().split()))
    arr2=list( map(int,input().split()))
    arr1 = [(arr1[i], i) for i in range(n)]
    arr1.sort()
    arr2.sort()
  
    ans=[0]*n

    for i in range(n):
        _, ind = arr1[i]
        ans[ind] = arr2[i]
  


    print(*ans)



