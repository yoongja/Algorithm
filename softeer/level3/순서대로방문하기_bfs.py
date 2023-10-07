from collections import deque


def bfs(start):
    global cnt
    queue = deque([(start, 0)])
    visited[start[1]][start[0]] = 1

    while queue:
        now, destIdx = queue.popleft()
        y, x = now

        if now == must_visit[destIdx]:
            if destIdx == m - 1:
                cnt += 1
                continue
            else:
                destIdx += 1

        for dy, dx in [[0,-1],[0,1],[1,0],[-1,0]]:
            ey = y + dy
            ex = x + dx

            if 0 <= ey < n and 0 <= ex < n and visited[ey][ex] == 0 and graph[ey][ex] == 0:
                visited[ey][ex] = 1
                queue.append(([ey, ex], destIdx))
                visited[ey][ex] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
must_visit = []
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    must_visit.append([b-1, a-1])

visited = [[0 for _ in range(n)] for _ in range(n)]
bfs(must_visit[0])
print(cnt)
