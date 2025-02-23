# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict
k=int(input())
arr=list(input())
arr= [int(i) for i in arr]
cursum=0
d=defaultdict(int)
d[0]=1
count=0
for num in arr:
    cursum+=num
    count+=d[cursum-k]
    d[cursum]+=1
    

print(count)
    
