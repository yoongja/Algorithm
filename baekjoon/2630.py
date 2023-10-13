n = int(input()) # 한변의 길이 n이 주어짐
# 2, 4, 8 , 16, 32, 64, 128
graph = [list(map(int,input().split())) for _ in range(n)]

# checker라는 함수 만들어서 확인하기
def checker(x,y,n):
    global blue, white
    cur = graph[x][y]
    bol = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur != graph[i][j]: # 같지 않은 부분이 나타난다면
                bol = False
                n = n // 2
                checker(x,y,n) # 1
                checker(x + n,y,n) # 2
                checker(x, y + n, n) # 3
                checker(x + n, y + n, n) # 4
                return # 만나자마자 더이상 for문 탐색안함
    if bol == True:
        if cur == 1: # 파란색으로 칠해진 칸
            blue += 1
        else : # 하얀색으로 칠해진 칸
            white += 1

blue = 0
white = 0
checker(0,0,n)
print(white)
print(blue)

