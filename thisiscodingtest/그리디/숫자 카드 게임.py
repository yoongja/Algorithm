N,M = map(int,input().split())
real_min = 0
for i in range(N):
    arr = list(map(int,input().split()))
    Min = min(arr)
    if real_min<Min:
        real_min = Min

print(real_min)
