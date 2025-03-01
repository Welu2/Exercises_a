# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B


n,k = map(int,input().split())
arr = list(map(int,input().split()))

l = 0
r = k

window = sum(arr[:k])
total = window

while r < len(arr):
    window += arr[r] - arr[l]
    total += window
    l += 1
    r += 1

print(f"{total/(n-k+1):.10f}")
