# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from itertools import accumulate


n, k, q = map(int, input().split())

LIMIT = 200001  

freq = [0] * (LIMIT + 1)


for _ in range(n):
    start, end = map(int, input().split())
    freq[start] += 1
    freq[end + 1] -= 1 

for i in range(1, LIMIT + 1):
    freq[i] += freq[i - 1]  


valid = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
    valid[i] = 1 if freq[i] >= k else 0


special = list(accumulate(valid))



for _ in range(q):
    start, end = map(int, input().split())
    print(str(special[end] - special[start - 1]))
