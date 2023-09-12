# 이거 배낭 알고리즘 이름 뭐였지 ㅋㅋㅋㅋㅋㅋ knapsack .. ? dp로 푸는건가 뭐였더라 ..,일단 브루트포스로 푸는건 아님
# 얘 잘라서 넣는거니까 ,greedy가능

# 금,은,백 귀금속 있음, 배낭 W까지 채울 수 있음
# 각 금속의 무게와 가격이 있을때, 배낭을 채울 수 있는 가장 값비싼 가격은 ?

result = 0
result_weight = 0
arr = []
Bag_Weight, Variety = map(int,input().split())
for _ in range(Variety):
    Gold_Weight, Gold_Price = map(int,input().split())
    arr.append([Gold_Weight,Gold_Price])
# arr을 무게당으로 정렬한다.
sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)
for i in range(len(sorted_arr)):
    result_weight += sorted_arr[i][0]
    if Bag_Weight >= result_weight:
        result += sorted_arr[i][0] * sorted_arr[i][1]
    else:
        result_weight -= sorted_arr[i][0]
        result += (Bag_Weight - result_weight) * sorted_arr[i][1]
print(result)

