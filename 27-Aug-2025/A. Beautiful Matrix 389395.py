# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

arr=[]
l=0
for i in range(5):
    a=list(map(int,input().split()))
    if a != [0,0,0,0,0]:
        arr=a
        l=i+1
 
i=arr.index(1)+1
 
print(abs(3-l)+abs(3-i))