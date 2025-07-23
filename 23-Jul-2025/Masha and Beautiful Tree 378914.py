# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def is_sortable(arr):
    if len(arr) == 1:
        return 0, arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    l_swaps, l_sorted = is_sortable(left)
    if l_swaps == -1:
        return -1, []

    r_swaps, r_sorted = is_sortable(right)
    if r_swaps == -1:
        return -1, []

    merged = l_sorted + r_sorted
    if merged == sorted(merged):
        return l_swaps + r_swaps, merged
    elif r_sorted + l_sorted == sorted(merged):
        return l_swaps + r_swaps + 1, r_sorted + l_sorted
    else:
        return -1, []

t = int(input())

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    ans, _ = is_sortable(p)
    print(ans)
