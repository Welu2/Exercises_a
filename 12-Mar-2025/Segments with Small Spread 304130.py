# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n,k = map(int,input().split())
nums=list(map(int,input().split()))
dec=deque()
inc=deque()
l=0
ans=0
for r in range(len(nums)):
    while dec and dec[-1] < nums[r]:
        dec.pop()
    dec.append(nums[r])
    while inc and inc[-1] > nums[r]:
        inc.pop()
    inc.append(nums[r])
   

    
    while dec[0]-inc[0] > k:
        val=nums[l]
        
        if inc[0] == val:
            inc.popleft()
        if dec[0] == val:
            dec.popleft()  
        l+=1

    ans+=(r-l+1)



print(ans)
