N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

arr = sorted(arr,reverse = True)

cnt = 0
ans = 0
i=0

while(True):
    ans += arr[0]
    cnt +=1
    i+=1
    if cnt == K:
        cnt = 0
        ans += arr[1]
        i += 1
    if i == M:
        break
        
print(ans)
