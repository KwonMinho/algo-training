def solution(s, n):
    answer = ''
    
    for c in s:
        c = ord(c)
        print(c)
        if c >= 97 and c <= 122:
            if c+n > 122: answer+=chr(c+n-26)
            else: answer+=chr(c+n)
        elif c >= 65 and c <= 90:
            if c+n > 90:
                print(c+n-26)
                answer+=chr(c+n-26)
            else: answer+=chr(c+n)
        else:
            answer += ' '
    
    return answer