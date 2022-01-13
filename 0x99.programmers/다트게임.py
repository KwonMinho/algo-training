
def solution(dart):
    answer = 0
    
    dart = list(dart)
    bonus_list = {'S': 1, 'D': 2, 'T': 3}
    is_before_star = False
    
    while dart:
        c = dart.pop()
        final_score = 0
        
        if c == '*' or c == '#':
            bonus = dart.pop()
            score = int(dart.pop()) 
            
            final_score = (score**bonus_list[bonus])
            
            if is_before_star: 
                final_score *=2
                is_before_star = False
            
            if c =='#': 
                final_score *=-1
            else: 
                final_score *=2
                is_before_star = True
            
        else:
            bonus = c
            score = int(dart.pop())
            if score == 0 and dart and dart[-1] == '1':
                dart.pop()
                score = 10
                
            final_score = score**(bonus_list[c])
            
            if is_before_star: 
                final_score *=2
                is_before_star = False
        
        answer += final_score
        
    
    return answer



    import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer