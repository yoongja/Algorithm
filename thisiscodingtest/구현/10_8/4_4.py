from collections import deque


def bfs(x,y,d):
    q = deque()
    q.append((x,y))
    cnt = 1 # 처음방문한곳 방문개수
    visited[x][y] = 1 # 처음 방문한곳 방문처리

    while q:
        cx, cy = q.popleft() # 현재 x,y
        flag = 1
        # 가보지 않은 칸 존재한다면, 회전후 왼쪽으로 한칸
        for _ in range(4):
            d = (d + 3) % 4
            nx = dx[d] + cx # next x
            ny = dy[d] + cy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 0: # 가보지 않았으며, 육지일 경우
                visited[nx][ny] = 1
                flag = 0 # 가보지 않은 곳이 존재한다는 것
                cnt += 1
                q.append((nx,ny))
                break
        if flag == 1 : # 4방향중 갈 곳이 없다는 것
            # 바라보는 방향을 유지한채, 한 칸 뒤로가고 1단계
            if graph[cx - dx[d]][cy - dy[d]] == 0 : # 후진한게 땅이라면
                q.append((cx - dx[d],cy - dy[d]))
            else: # 바다라 돌아갈 수 없으면 움직임 멈춤
                print(cnt)
                break

    

n, m = map(int,input().split())
s_x,s_y,s_d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
d = [0,1,2,3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
bfs(s_x,s_y,s_d)