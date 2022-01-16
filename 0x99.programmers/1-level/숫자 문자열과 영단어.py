def isChar(c):
    if ord(c) >= 97 and 122 >= ord(c): return True
    else: return False
    

def solution(str):
    answer = ''
    
    d = {
        'zero': '0',
        'one': '1',
        'two':'2',
        'three': '3',
        'four':'4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    # 1. 현재 문자가 숫자 문자인지 아닌지를 구분한다.
    # 2. 숫자라면, answer 에 더해준다.
    # 3. 문자라면, 문자가 끝날때까지 tmp에 담아준다.
    
    tmp = ''
    for i,s in enumerate(str):
        if isChar(s):
            tmp += s
            if tmp in d:
                answer += d[tmp]
                tmp = ''
        else:
            answer += s
        
    return int(answer)