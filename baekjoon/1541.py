#괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성

str = input().split('-')
sum = 0
#마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 더해서 뺴기
for i in range(len(str)):
    part_sum = 0
    new = str[i].split('+')
    for j in new:
        part_sum += int(j) # 원소 더하기
    #처음은 더하고 두번째 원소부터 빼기
    if i == 0:
        sum += part_sum
    else:
        sum -= part_sum
print(sum)
