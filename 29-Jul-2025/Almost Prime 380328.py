# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n=int(input())
def count_distinct_prime_factors(num):
    count = 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            count += 1
            while num % i == 0:
                num //= i
        i += 1
       
    if num > 1:
        count += 1
    return count
ans=0

for i in range(1,n+1):
    if count_distinct_prime_factors(i) == 2:
        ans+=1
print(ans)
