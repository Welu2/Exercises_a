# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

n,m = map(int,input().split())
parent=[i for i in range(n+1)]
experience=[0]*(n+1)
difference=[0]*(n+1)
size=[1]*(n+1)

def find(node):
    
    if node != parent[node]:
        originalp=parent[node]
        parent[node]=find(parent[node])
        difference[node]+=difference[originalp]
    return parent[node]

def union(u,v):
    U=find(u)
    V=find(v)
    if U != V:
        if size[U] < size[V]:
            U,V= V,U

        parent[V]=U
        difference[V]=difference[V] + experience[V] - experience[U]
        size[U]+=size[V]  

for _ in range(m):
    command= list(input().split())
    if command[0] == "add":
        u,ex=int(command[1]),int(command[2])
        a=find(u)
        experience[a]+=ex
     
    elif command[0]=="join":
        u,v=int(command[1]),int(command[2])
        union(u,v)

    else:
        u=int(command[1])
        find(u) 
        print(experience[find(u)]+difference[u])

