N, K = map(int,input().split())

arr = [] #가치를 넣어두기 위한 배열
rest = K #남은 금액 계속해서 갱신
cnt = 0 #최소 동전개수

for _ in range(N):
    i = int(input())
    arr.append(i)

arr.sort(reverse=True)#내림차순

for i in arr:
    if i<=K:
        while(True):
            cnt += rest//i
            rest %=i
            if i>rest:
                break
          
    if rest == 0:
        break

print(cnt)

        