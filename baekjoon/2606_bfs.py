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

q = deque()

q.append(1) # 처음 q에 내가 출발할 노드 넣어줌

while len(q) > 0 : # q가 0이된다면 멈출거야!
    node = q.popleft() # 1
    visited[node] = 1 # 가지고 온 친구는 방문처리

    for nxt in graph[node]: # 그래프에 있는 노드위치에 있는걸 전부 꺼내줌
        if visited[nxt] == 1: # 만약 내가 이친구를 방문한적 있다면
            continue
        q.append(nxt)

print(sum(visited) - 1)