from collections import deque

n = int(input()) # 정사각형, 가로와 세로의 크기 (5<=n<=25)

graph = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
result = []
for y in range(n):
    for x in range(n):
        cnt = 0
        if visited[y][x] == 1: # 이미 방문했다면 안봄
            continue
        if graph[y][x] == '1':

            # BFS
            q = deque()
            q.append((y,x))
            visited[y][x] = 1

            while q:
                ey,ex = q.popleft()
                # 4 방향 탐색
                for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ny, nx = ey + dy , ex + dx
                    if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == '1' and visited[ny][nx] == 0: # 방문하지 않았고, 범위안에 들고,1이라면
                        visited[ny][nx] = 1
                        q.append((ny,nx))
                        cnt += 1
            result.append(cnt)

result.sort()
print(len(result))
for ans in result:
    print(ans + 1)
