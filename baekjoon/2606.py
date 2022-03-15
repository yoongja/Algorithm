from collections import deque

n = int(input())
p = int(input())


graph = [[] for _ in range(n+1)]

for _ in range(p):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(graph,v,visited,cnt):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i]=True
    print(cnt)


visited = [False]*(n+1)
cnt = 0
bfs(graph,1,visited,cnt)
