# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

n,m,k= map(int,input().split())
parent=[i for i in range(n+1)]
size=[1]*(n+1)


def find(node):
    while node != parent[node]:
        parent[node]=parent[parent[node]]
        node=parent[node]
    return parent[node]

def union(u,v):
    U=find(u)
    V=find(v)

    if U != V:
        U,V=V,U
    parent[V]=U
    size[U]+=size[V]

edges=[]
for _ in range(m):
    u,v=map(int,input().split())
    edges.append((min(u, v), max(u, v)))
    

operations = []
cut_edges = set()
for _ in range(k):
    command,u,v= input().split()
    u=int(u)
    v=int(v)
    u, v = min(u, v), max(u, v)
    operations.append((command, u, v))
    if command == "cut":
        cut_edges.add((u, v))


# Process operations in reverse
answers = []
for cmd, u, v in reversed(operations):
    if cmd == "ask":
        answers.append("YES" if find(u) == find(v) else "NO")
    else:  # "cut" reversed = add edge back
        union(u, v)

# Print answers in original order
for ans in reversed(answers):
    print(ans)
    
