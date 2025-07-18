# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = int(input())
parents = [int(input()) for _ in range(n - 1)]

# Build adjacency list
from collections import defaultdict

children = defaultdict(list)

for i, p in enumerate(parents):
    parent = p
    child = i + 2  # since the child is i+2 (as i from 0 to n-2)
    children[parent].append(child)

is_spruce = True

for node in range(1, n + 1):
    if node in children:  # non-leaf node
        leaf_children = 0
        for ch in children[node]:
            if ch not in children:  # it's a leaf
                leaf_children += 1
        if leaf_children < 3:
            is_spruce = False
            break

print("Yes" if is_spruce else "No")
