# 회의실은 9시부터 18시 까지만 사용가능
# 한 회의실을 연속한 일정 시간 동안만 점유 가능
# 회의실, 시작 시각, 종료 시각 정보로 나타낼 수 있음
# 같은 회의실 사용하는 회의 시간은 서로 겹칠 수 없음
# 시작 시각과 종료 시각이 동일한 회의는 예약 x, 새롭게 잡을 수도 없음

class_num , reserve_num = map(int,input().split())
class_name = {}
time = ["09","10","11","12","13","14","15","16","17","18"]

for _ in range(class_num):
    class_name[input()] = [False for i in range(9)]
# 딕셔너리로 클래스 이름과 키값으로 9시는 0,18시는 8의 인덱스를 가짐

for _ in range(reserve_num):
    reserve_name, start, end = input().split()
    start = int(start) - 9
    end = int(end) - 9
    for i in range(start, end):
        class_name[reserve_name][i] = True


sorted_class_name = dict(sorted(class_name.items()))
arr_class_name = list(sorted_class_name)
for name, key in sorted_class_name.items():
    print(f'Room {name}:')
    available = []
    if False not in key:
        print("Not available")
    else:
        idx = 0
        while idx < 9:
            if key[idx] == False:
                start = idx
                while idx < 9 and not key[idx]:
                    idx += 1
                end = idx - 1
                available.append([start,end])
            idx += 1
        print(f'{len(available)} available:')
        for arr in available:
            print(f'{time[arr[0]]}-{time[arr[1] + 1]}')
    if arr_class_name[-1] != name:
        print("-----")