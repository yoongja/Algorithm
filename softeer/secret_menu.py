def check_secret(secret_key,person_num,button_num,secret_arr,person_arr):
    check = False
    for i in range(person_num):
        if person_arr[i] == secret_arr[0]: # 첫 숫자가 같다면
            idx = i
            for j in secret_arr:
                if idx == person_num:
                    check = False
                    break
                else:
                    if person_arr[idx] == j:
                        check = True
                        idx+=1
                    else:
                        check = False
                        break
            if check == True:
                print("secret")
                return
    print("normal")

secret_key, person_num, button_num = map(int,input().split()) # 비밀자판개수, 사용자 누른 개수,버튼 개수
secret_arr = list(map(int,input().split()))
person_arr = list(map(int,input().split()))
check_secret(secret_key,person_num,button_num,secret_arr,person_arr)