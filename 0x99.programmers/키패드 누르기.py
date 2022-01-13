def distance(n1,n2):
    n1 -=1
    n2 -=1
    return abs((n1//3)-(n2//3))+abs(n1%3-n2%3)
   
def solution(numbers, hand):
    answer = ''
    cur_left = 10
    cur_right = 12
    
    for n in numbers:
        if n == 0: n = 11
        if n%3 == 1:
            answer += 'L'
            cur_left = n
            continue
        elif n%3 == 0:
            answer += 'R'
            cur_right = n
            continue

        r_dt = distance(cur_right, n)
        l_dt = distance(cur_left, n)
        
        if r_dt < l_dt:
            answer += 'R'
            cur_right = n
        elif r_dt > l_dt:
            answer += 'L'
            cur_left = n
        else:
            if hand == 'right':
                answer += 'R'
                cur_right = n
            else:
                answer += 'L'
                cur_left = n
    
    return answer