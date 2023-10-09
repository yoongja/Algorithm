from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        nx, ny = q.popleft()
        for dx, dy in [[1,0],[-1,0],[0,-1],[0,1]]:
            ex, ey = nx + dx, ny + dy
            if 0 <= ex < n and 0 <= ey < n:
                if graph[ex][ey] == '1' and visited[ex][ey] == 0:
                    visited[ex][ey] = 1
                    q.append((ex,ey))
                    cnt += 1
    return cnt

n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)]for _ in range(n)]
arr = []
for x in range(n):
    for y in range(n):
        if visited[x][y] == 1:
            continue
        if graph[x][y] == '1':
            arr.append(bfs(x,y))
# bfs(0,0)
arr.sort()
print(len(arr))
for i in arr:
    print(i)