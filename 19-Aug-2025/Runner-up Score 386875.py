# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ma = max(arr)
    m = arr.count(ma)
    if m == 1:
        arr.remove(ma)
    else:
        for k in range(m):
           arr.remove(ma) 
    sec = max(arr)
    print(sec)
