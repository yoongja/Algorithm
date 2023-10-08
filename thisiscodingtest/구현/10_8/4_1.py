n = int(input())
direction = list(input().split())

d = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x, y = 0, 0
for next in direction:
    for idx in range(len(d)):
        if next == d[idx]: # 명령어가 d에있는 것과 같다면, idx저장
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n : # 지도 벗어나지 않을때만
                x, y = nx, ny # 이동해라!

print(x + 1,y + 1)
