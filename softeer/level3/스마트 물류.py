n, k = map(int,input().split()) # 라인의 길이, 잡을 수 있는 거리
p_h = list(input()) # p-> 로봇, h -> 부품
visited = [0 for _ in range(n)]
cnt = 0
for i in range(n):
    if p_h[i] == 'P':
        for j in range(i - k, i + k + 1):
            if j >= n or j < 0:
                continue
            if p_h[j] == 'H' and visited[j] == 0:
                visited[j] = 1
                cnt += 1
                break

# 완전 탐색
print(cnt)