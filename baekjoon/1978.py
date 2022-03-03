N = int(input())

arr = list(map(int,input().split(' ')))#소수 판별 리스트

cnt = 0 
arr_tf =[]
tf_count = 0

for i in arr:
    tf = True
    if i != 1:
        for j in range(2,i):
            if i % j == 0 :
                tf = False
                break
    else:
        tf = False
    arr_tf.append(tf)

for i in range(N):
    if arr_tf[i]==True:
        tf_count += 1
print(tf_count)

            
