# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

from collections import defaultdict


t = int(input())
word = input()
d = defaultdict(int)
output = []
for i in word:
    d[i] += 1

for j in d:
    if j == 'n':
        b='1'*d[j]
        output.append(' '.join(b) )
for j in d:
    if j == 'z':
        a = '0'*d[j]
        output.append(' '.join(a))
print(*output)
