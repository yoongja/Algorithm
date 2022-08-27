n,m = map(int,input().split())
arr = [[] for _ in range(n)] #n행을 만듦

for i in range(n):
    for j in range(m): #m열을 받음
        wb = input()
        arr[i][j].append(wb)

for _ in range(n):
    if arr[0][0] == "W":
        
    if arr[0][0] == "B":
        