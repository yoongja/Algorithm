n = int(input())

dx = [0,0,-1,1]#왼,오,위,아래
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
x,y = 1,1
plans = input.split()

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue #정사각형을 벗어나는 움직임은 무시된다
    x,y = nx,ny
print(nx,ny)