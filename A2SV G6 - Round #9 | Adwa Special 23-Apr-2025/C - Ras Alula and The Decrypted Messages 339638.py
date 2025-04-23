# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    d=input()
    w=input()
    flag=False
    expected=0
    current=0
    for i in w:
        expected+=ord(i)

    for j in range(k):
        current+=ord(d[j])

    if current == expected:
        flag=True
    for j in range(k,n):
        current+=ord(d[j])
        current-=ord(d[j-k])
        if current == expected:
            flag=True
    
    if flag:
        print("YES")
    else:
        print("NO")
   
