# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
if sum(arr1) != sum(arr2):
    print(-1)
else:
    cursum1,cursum2=0,0
    l1,l2=0,0
    ans=0
    while l1 < n1:
        cursum1+=arr1[l1]
        cursum2+=arr2[l2]
        l1+=1
        l2+=1

        while cursum1 != cursum2:
            if cursum1 < cursum2:
                cursum1+=arr1[l1]
                l1+=1
            else:
                cursum2+=arr2[l2]
                l2+=1
        ans+=1
       
    
    print(ans)

