# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n,m= map(int,input().split())
arr=list(map(int,input().split()))
a={}
l=0
c=[0, 0]

t=0
for right in range(n):
    a[arr[right]]=a.get(arr[right],0)+1
    
    while len(a) > m and l < n:
        a[arr[l]]-=1
        if a[arr[l]] ==0:
            del a[arr[l]]
        l+=1
    
    if  right-l > c[1]-c[0]:
         c=[l,right]
    


      
print(c[0]+1,c[1]+1)

