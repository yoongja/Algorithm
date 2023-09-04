# 바이러스가 숙주 몸속에서 p배씩 증가
# 처음 k마리 있었다면, N초 후에는 총 몇 마리의 바이러스 ? 

first_virus, percent, total_time = map(int,input().split())
total_virus = first_virus
for _ in range(total_time):
    total_virus *= percent
    total_virus %= 1000000007
print(total_virus)