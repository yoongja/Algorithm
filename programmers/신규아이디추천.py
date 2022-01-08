def solution(new_id):
    answer = ''
    id = new_id
    id = id.lower() #1단계
    #2단계
    for i in id:
        if i.isalpha():
            answer+=i
        if i.isdigit():
            answer+=i
        if i == '-':
            answer+=i
        if i == '_':
            answer+=i
        if i == '.':
            answer+=i
  
    #3단계
    temp = ""
    l = len(answer)
    for i in range(0,l):
        if answer[i] == ".":               
            if answer[i-1] != answer[i]:
                temp += answer[i]
            else:
                continue
        else:
            temp += answer[i]
    if len(answer)!=1:
        answer = temp

     #4단계
    l = len(answer)
    if l == 1:
        if answer[0]==".":
            answer = ""
    else:
        if answer[0]==".":
            answer = answer[1:l]
        l = len(answer)
        if answer[l-1] == ".":
            answer = answer[0:l-1]

     #5단계
    if answer == "":
        answer+="a"
        
    #6단계
    if len(answer)>=16:
        answer = answer[0:15]
    l = len(answer)
    if answer[l-1]==".":
        answer = answer[0:l-1]
        
    #7단계
    l = len(answer)
    if len(answer)<=2:
        temp = answer[l-1]
        for i in range(l-1,2):
            answer+=temp

    
    return answer