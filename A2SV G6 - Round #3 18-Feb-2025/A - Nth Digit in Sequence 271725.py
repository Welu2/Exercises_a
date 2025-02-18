# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n=int(input())
arr=[]
for i in range(1,1001):
    arr.append(f'{i}')
 
arr="".join(arr)
print(arr[n-1])