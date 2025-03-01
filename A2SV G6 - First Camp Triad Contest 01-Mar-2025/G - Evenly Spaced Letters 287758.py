# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

from collections import defaultdict


t = int(input())
for _ in range(t):
    word = input()
    d = defaultdict(int)

    wordl = []

    for i in range(len(word)):
        d[word[i]] += 1

    for j in d:
        if d[j] == 2:
            wordl.append(j)
            wordl.append(j)

    for j in d:
        if d[j] == 1:
            wordl.append(j)
    print(''.join(wordl))
