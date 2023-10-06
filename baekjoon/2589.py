from collections import deque

Y, X = map(int,input().split())

graph = [list(input()) for _ in range(Y)]

# 처음부터 끝까지 다 갈것, 해당 위치가 어디인지 찾으러 생각하는게 아님
# 그냥 가장먼거리가 나오면, 그게 보물의 위치라고 생각하고 이를 최단거리로 정답 출력함

maxi = 0
for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            # 좌표가 달라질때 마다 바껴야 하기 때문
            visited = [[0 for _ in range(X)] for _ in range(Y)]
            # 거리를 새로 계산해줌
            dist = [[0 for _ in range(X)] for _ in range(Y)]
            q = deque()
            q.append((y,x))
            visited[y][x] = 1
            cnt = 0
            while q:
                ey,ex = q.popleft()
                # 4 방향 탐색
                for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ny, nx = ey + dy , ex + dx
                    if 0 <= ny < Y and 0 <= nx < X and graph[ny][nx] == 'L' and visited[ny][nx] == 0:
                        q.append((ny,nx))
                        visited[ny][nx] = 1
                        # 내가 지금 있는 거리에서 더하기 1을 한다
                        dist[ny][nx] = dist[ey][ex] + 1
                        # 그럴때마다, maxi라는 친구를 업데이트 한다!
                        maxi = max(maxi, dist[ny][nx])

print(maxi)
