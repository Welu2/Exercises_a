# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

n,k = map(int,input().split())
while k > 0:
    lastD=n%10
    if lastD > 0:
        n-=1
       
    else:
        n=n//10
    k-=1
 
print(n)