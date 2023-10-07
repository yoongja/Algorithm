import bisect

n, q = map(int,input())
car = list(map(int,input().split())) # 자동차 연비에 해당하는 값, 모두 서로 다름
car.sort()
setCar = set(car)
for _ in range(q):
    m = int(input())
    if m not in setCar:
        print(0)
    else:
        idx = bisect.bisect_left(car, m)
        print(idx * (n-idx-1))