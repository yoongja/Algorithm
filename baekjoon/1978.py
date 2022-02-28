
N = int(input())

arr = list(map(int,input().split(' ')))#소수 판별 리스

tf = False
cnt = 0 #소수개수 구하기

for i in arr: #arr숫자 하나씩 비교
    if i != 1:
        for j in range(2,i):#시간복잡도 고려 하여 제곱근까지
            if i%j==0:
                break
            else:
                cnt += 1

print(cnt)
            
