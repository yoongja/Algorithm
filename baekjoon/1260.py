from collections import deque
from turtle import Turtle

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v,visited):
    print(v,end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,visited)

def bfs(v,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True



visited=[False]*(n+1)
dfs(v,visited)
print()
visited=[False]*(n+1)
bfs(v,visited)