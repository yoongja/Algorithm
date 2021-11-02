def solution(s):
    number = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,letter in enumerate(number):
        if letter in s:
            s = s.replace(letter,str(i))
    return int(s)