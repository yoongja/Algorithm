all_money = int(input())
arr_sum = 0
for _ in range(9):
    money = int(input())
    arr_sum += money

print(all_money-arr_sum)

