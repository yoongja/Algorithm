def solution(w,h):
    w_list=[]#가로, 세로의 약수를 저장할 리스트
    h_list=[]
    for i in range(1,w+1): #약수 저장
        if w%i==0:
            w_list.append(i)
    #print(w_list)
    for i in range(1,h+1):
        if h%i==0:
            h_list.append(i)
    #print(h_list)
    hw_list = set(w_list).intersection(h_list)#두 리스트의 중복값을 리스트에 저장
    return w*h-(w+h-max(hw_list)) #중복값이 저장된 리스트에서 가장 큰 값을 반환