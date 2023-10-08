# 럭키 스트레이트 -> 점수가 특정 조건 만족할때 사용
# 특정조건 -> 현재 캐릭터 점수 N, 점수 N을 자릿수 기준으로 반으로 나눔
# 반 나눈 왼쪽, 오른쪽 같은것!

arr = list(input())
# 항상 짝수 형태
n = len(arr) // 2
l, r = list(map(int,arr[:n])), list(map(int,arr[n:]))
# lamda 함수 .. ?
if sum(l) == sum(r):
    print("LUCKY")
else:
    print("READY")