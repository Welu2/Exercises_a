# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m=map(int,input().split())
arr=[]
flag=True
for _ in range(n):
    arr.append(list(input()))

def calulate(a,b,arr):
    d=[[a-1,b-1], [a-1,b], [a-1,b+1], [a,b-1],[a,b+1],[a+1,b-1],[a+1,b+1],[a+1,b]]
    
    count=0
    for val in d:
        
        if 0<= val[0] < n and 0<= val[1]< m:
            
            if arr[val[0]][val[1]] == "*":
                count+=1
    return count

for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":
            continue
        if arr[i][j] == '.':
            if calulate(i,j,arr) > 0:
                flag=False
        if arr[i][j].isdigit() :
             if calulate(i,j,arr) != int(arr[i][j]):
                 flag=False

      

if flag:
    print("YES")
else:
    print("NO")


