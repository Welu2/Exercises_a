# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

n=int(input())

for _ in range(n):
    index=0
    count=0
    a=input()
    while index<=9:
        if a[index] != "codeforces"[index]:
            count+=1
        index+=1

    print(count)