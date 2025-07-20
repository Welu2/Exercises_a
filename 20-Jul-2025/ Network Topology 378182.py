# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
n,e = list(map(int,input().split()))
d=defaultdict(list)

def topology(graph):
    flag=True
    o=0
    for i in range(1,n+1):
        if len(graph[i]) == 1 :
            o+=1
        elif len(graph[i]) == 2:
            continue
        else:
            flag=False
    if flag and o == 2:
        return "bus topology"
    else:
        flag=True
        if all(len(graph[i]) == 2 for i in range(1,n+1)):
            return "ring topology"
        c=0
        for i in range(1,n+1):
            if len(graph[i]) == 1:
                continue
            elif len(graph[i]) == n-1:
                c+=1
            else:
                flag=False
        if flag and c==1:
            return "star topology"
        else:
            return "unknown topology"
    

for _ in range(e):
    u,v=list(map(int,input().split()))
    d[u].append(v)
    d[v].append(u)
print(topology(d))

 