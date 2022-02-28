#세자리만 체크하기

N = int(input())
cnt = 0

if N <100:#세자리수 미만이면 개수 동일
    print(N)

else:
    for i in range(100,N+1):
        num_list = list(map(int,str(i))) #i를 리스트로 변경
        if num_list[0]-num_list[1]==num_list[1]-num_list[2]:#각 자리수 빼기가 같은지를 판단
             cnt += 1

    print(cnt+99)
