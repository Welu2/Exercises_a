# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

r,c=map(int,input().split())
 
flag=True
for i in range(r):
    if i % 2 ==0:
        print('#'*c)
    else:
        if flag:
            print('.'*(c-1)+"#")
            flag=False
        else:
            print('#'+'.'*(c-1))
            flag=True
 