from collections import deque

queue = deque()

computer = int(input())
connection = int(input())
graph = [[]for _ in range(computer + 1)] # computer 수보다 1대많게
visited = [0 for _ in range(computer + 1)]

for _ in range(connection):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)
recur(1)
print(sum(visited)-1)

