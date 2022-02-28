N = int(input())
ans = 0


for i in range(1,N+1): #i가 1부터 이므로 가장처음 n이 되었을때가 가장작은 생성자
    digit_sum = sum(map(int,str(i)))
    ans = i + digit_sum
    if ans == N:
        print(i)
        break

    if i==N:
        print(0) #i가 반복문을 탈출하지 못한 채 끝까지 반복을 수행한 경


