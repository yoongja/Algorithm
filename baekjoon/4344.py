C = int(input())
for i in range(C):
    Sum = 0
    avg = 0
    new_avg = 0
    arr = list(map(int,input().split()))
    N = arr[0] #학생수
    for j in range(1,len(arr)): #학생수 제외한 순서부터
        Sum += arr[j]
        
    avg = Sum/N #평균

    for j in range(1,len(arr)):
        if arr[j]>avg:
            new_avg += 1 #평균을 넘는 학생수 더하기 

    new_avg = (new_avg/N)*100
    print(f"{new_avg:.3f}%") #소수점3자리까지 출력
