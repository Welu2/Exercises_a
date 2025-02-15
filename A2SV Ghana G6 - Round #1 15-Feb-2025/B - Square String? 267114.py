# Problem: B - Square String? - https://codeforces.com/gym/585132/problem/B

n=int(input())
for _ in range(n):
    s=input()
    a=len(s)
    if s[:a//2] == s[a//2:]:
        print('YES')
    else:
        print('NO')