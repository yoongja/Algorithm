from collections import deque
import queue

n,m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs():
    cnt = 0
    x,y =0,0
    queue = deque([(x,y)]) #튜플
    cnt += 1
    while queue: #queue가 끝나기 전까지 모두모두 빨아먹을것
        
        x,y = queue.popleft() #튜플사용
        for i in range(4): #상하좌우이므로
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                cnt += 1
                queue.append((nx,ny))
                graph[nx][ny]=0

    print(cnt)

bfs()    
            
