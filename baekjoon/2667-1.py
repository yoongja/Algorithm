from collections import deque

queue = deque()

n = int(input())

graph = []
num = [] #각 단지의 수를 위한 배열
count = 0 #각단지수를 더하기 위한 변수
result = 0 #총단지수

for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue.append((x,y))
    if graph[x][y] == 1:
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<=-1 or nx >=n or ny<=-1 or ny>=n: #범위 나가면 검사안하기
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    global count
                    count += 1
                    queue.append((nx,ny))
                    graph[nx][ny] = 0 #방문처리해주기
        return True
    return False

for i in range(n):
    for j in range(n):
        if bfs(i,j) == True:
            result += 1
            num.append(count) #단지수를 추가해주기
            count = 0

print(result) #총 단지수 출력
num.sort()
for i in range(len(num)):
    print(num[i])

