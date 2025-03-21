# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t=int(input())
def check(c):
    l=0
    r=len(s)-1
    deleted=0
    while l < r:
        if s[l] != s[r]:
            if s[l] == c:
                l+=1
                deleted+=1
            elif s[r] == c:
                r-=1
                deleted+=1
            else:
                return float('inf')

        else:
            l+=1
            r-=1
    return deleted
for _ in range(t):
    n=int(input())
    s=input()
    is_pali=True
    l,r=0,n-1
    while l < r:
        if s[l] != s[r]:
            is_pali=False
            break
        else:
            l+=1
            r-=1
    if is_pali:
        print(0)

    else:
        
        ans=min(check(s[l]),check(s[r]))

        if ans == float("inf"):
            print(-1)
        else:
            print(ans)
