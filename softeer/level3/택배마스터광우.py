# 순열을 이용하기
import sys
from itertools import permutations

lail, baguni, k = map(int,input().split()) # 레일개수, 바구니 무게, 시행해야 하는 횟수
weight = list(map(int,input().split()))
# 모두 다 넣어보고, 가장 적은 것을 답으로 한다!
rails_info = permutations(weight,lail)
result = sys.maxsize
for now_rails in rails_info:
    rails = list(now_rails)
    cnt = 0
    i = 0
    bucket = 0
    all = 0
    while cnt != k:
        if bucket + rails[i] <= baguni: # 바구니 보다 적다면, 하나 늘려주기
            bucket += rails[i]
            rails.append(rails[i])
            i += 1
        else: # 바구니 무게를 넘는다면, 일한 횟수를 올려주기
            cnt += 1
            all += bucket
            bucket = 0
    result = min(result,all)

print(result)