def num_to_list(num):
    num_arr = [10] * (5 - len(num)) + [int(x) for x in num]
    return num_arr

# a와 b는 숫자 0으로 시작하지 않고, 서로 다르다.
test_case = int(input())
# 숫자마다 7개짜리 배열을 만들고 거기에 순서를 부여, true와 false로 구분하고 서로 다른 부분을 차이점으로 잡기
# A와b는 최대 5자리수임

# 숫자빼고임!!!
num = [
    [True,True,False,True,True,True,True],
    [False,True,False,True,False,False,False],
    [True,True,True,False,True,True,False],
    [True,True,True,True,True,False,False],
    [False,True,True,True,False,False,True],
    [True,False,True,True,True,False,True],
    [True,False,True,True,True,True,True],
    [True,True,False,True,False,False,True],
    [True,True,True,True,True,True,True],
    [True,True,True,True,True,False,True],
    [False,False,False,False,False,False,False]
    ]
for _ in range(test_case):
    result = 0
    a, b = input().split()
    # 5칸 짜리 배열을 선언하기
    a_num = num_to_list(a)
    b_num = num_to_list(b)
    print(a_num)
    for j in range(5):
        for i in range(7):
            if num[a_num[j]][i] != num[b_num[j]][i]:
                result += 1
    print(result)
