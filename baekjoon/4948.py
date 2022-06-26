#자연수 n 보다 크고,2n보다 작거나 같은 소수는 적어도 하나 존재한다

#각 테스트 케이스에 대해서 ,n보다 크고 2n보다 작거나 같은 소수의 개수
#소수 판별 알고리즘 사용해야함

def is_prime(arr,arr_bool):
    sum = 0
    idx = 0
    for i in arr:
        for j in range(2,int(i**(1/2))+1):#제곱근까지 하여 시간복잡도를 O(루트n)
            #print(f'나누는수{j}')
            #print(f'현재i{i}')
            if i % j == 0:
                arr_bool[idx] = True
                break
        idx += 1
    #print(arr_bool)
    return arr_bool.count(False)
        
                    
    
    

while(True):
    num = int(input())
    if num == 0:
        break
    arr = []
    arr_bool = []
    for i in range(num+1,num*2+1):
        arr.append(i)
        arr_bool.append(False)
    #print(f'현재배열에는{arr}')
    sum = is_prime(arr,arr_bool)
    print(sum)