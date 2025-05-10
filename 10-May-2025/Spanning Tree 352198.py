# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

n,m =map(int,input().split())
o=[]
total=0
for _ in range(m):
    o.append(list(map(int,input().split())))
edges=sorted(o, key=lambda a: a[2])

parent=[i for i in range(n+1)]
rank=[0]*(n+1)
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(u,v):
    U=find(u)
    V=find(v)
    if U  == V:
        return False
    if rank[U] < rank[V]:
        parent[U]=V
    else:
        parent[V]=U
        if rank[U] == rank[V]:
            rank[U]+=1

    return True
edges_used=0
for u,v,w in edges:
    if (union(u,v)):
        total+=w
        edges_used += 1
        if edges_used == n - 1:
            break

print(total)

