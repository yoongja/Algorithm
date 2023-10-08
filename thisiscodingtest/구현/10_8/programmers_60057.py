def solution(s):
    first = s
    for section in range(1,len(s) // 2 + 1):
        ans = ""
        cnt = 1
        prev = s[:section]
        # idx 범위 확인하기
        for current in range(section,len(s),section):
            if s[current:current+section] == prev: # 만약같다면
                cnt += 1
            else : # prev와 더이상 같지 않다면
                if cnt >= 2:
                    ans = ans + str(cnt)+ prev
                else:
                    ans += prev 
                prev = s[current:current+section] # prev변경해주기
                cnt = 1
        # 남아있는 문자열에 대해서 처리
        if cnt >= 2:
            ans += str(cnt) + prev
        else:
            ans += prev

        ans = min(len(first), len(ans))
    return ans

print(solution("aabbaccc"))