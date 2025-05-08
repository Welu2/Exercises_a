# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

for _ in range(t):  
    n, x = map(int, input().split())    
    nums = sorted(map(int, input().split()), reverse=True)   
    
    total = 0   
    for i in range(n):  
        total += nums[i]  
        if total < x * (i + 1):  
            print(i)  
            break  
    else:  
        print(n)    