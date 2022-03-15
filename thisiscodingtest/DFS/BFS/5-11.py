from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft() #인접노드의 상하좌우를 구경하게 된다

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue #괴물 만났을때 멈춤
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #바로 직전거리 위치에서 1을 더한값을 넣어준다
                queue.append((nx,ny))
    return graph[n - 1][m - 1] #가장 오른쪽 아래까지의 최단 거리 반환한다.

print(bfs(0,0))