n = int(input())
arr_number = [] #단지수를 입력받는 배열
arr = []


for i in range(n):
    arr.append(list(map(int,input())))

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if arr[x][y] == 1: #1일 경우에는 상하좌우를 검색할 것
        global count
        count += 1
        arr[x][y] = 0 #방문 처리해주기
        
        dfs(x,y-1) #상
        dfs(x,y+1) #하
        dfs(x-1,y) #좌
        dfs(x+1,y) #우
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n): #각 노드 마다 검색할 것
        if dfs(i,j) == True:
            arr_number.append(count)
            count = 0 
            result += 1

print(arr)
arr_number.sort()
print(result)
for i in range(len(arr_number)):
    print(arr_number[i])