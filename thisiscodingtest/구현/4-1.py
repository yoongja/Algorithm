N = int(input())
plan = input().split()

X,Y=1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
draw = ['L','R','U','D']

for i in plan:
    find= draw.index(i)
    
    if X+dx[find]<1 or Y+dy[find]<1 or X+dx[find]>N or Y+dy[find]>N:
        continue

    X = X+dx[find]
    Y = Y+dy[find]

print(X,Y)
