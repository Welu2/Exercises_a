# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D


import heapq


p,m=map(int,input().split())
graph=[[] for _ in range(p)]
incoming =[0 for i in range(p)]
for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1

    graph[u].append(v)
    incoming[v]+=1

heap = []
for i in range(p):
    if incoming[i] == 0:
        heapq.heappush(heap, i)


ans=[]

while heap:
    
        c= heapq.heappop(heap)
                
        ans.append(c)
        for h in graph[c]:
            incoming[h]-=1
            if incoming[h]==0:
                heapq.heappush(heap,h)

if len(ans) != p:
    print(-1)
else:
    print(*[x + 1 for x in ans])
    

            