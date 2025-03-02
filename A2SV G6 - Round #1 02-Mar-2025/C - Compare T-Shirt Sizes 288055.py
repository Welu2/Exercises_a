# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

n=int(input())

for _ in range(n):
    a,b = input().split()
    if a[-1] == 'S'  and b[-1] != 'S':
        print("<")
    elif a==b:
        print("=")
    elif a[-1] != 'S'  and b[-1] == 'S':
        print(">")
    elif a[-1] =='S' and b[-1] == 'S':
        if len(a) > len(b):
            print("<")
        elif len(a) < len(b):
            print(">")
        
    elif a[-1] =='L' and b[-1] == 'L':
        if len(a) < len(b):
            print("<")
        elif len(a) > len(b):
            print(">")
       
    elif a[-1] == 'M'  and b[-1] == 'L':
        print("<")
    elif a[-1] == 'L'  and b[-1] == 'M':
        print(">")
     


