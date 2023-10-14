from collections import deque

n, k = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0 for _ in range(n)])
result = 0
# 내구도와 로봇의 여부가 중요함
# 내구도가 0인 칸의 개수 k 개 이상이라면, 과정 종료
# 즉시 1만큼 감소

while 1:
    result += 1
    # 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 # 로봇의 마지막 인덱스는 로봇을 내리는 위치이므로 0

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 내리는 위치 이전부터 올리는 위치까지 반복문 범위로 잡아 값 하나씩 확인
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[-1] = 0 # 마지막 칸에 있는 친구는 내려준다
    # 올리는 위치에 로봇이 없고 내구도 1이상이라면 해당 위치에 로봇 올림
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= k:
        break

print(result)
