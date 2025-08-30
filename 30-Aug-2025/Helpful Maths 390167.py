# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

s=input()
a=[]
for i in s:
    if i != "+":
        a.append(int(i))
 
a.sort()
ans=[]
for j in range(len(a)):
    if j != len(a)-1:
        ans.append(str(a[j]))
        ans.append("+")
    else:
        ans.append(str(a[j]))
 
print("".join(ans))
 