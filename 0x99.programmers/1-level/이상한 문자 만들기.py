https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = ''
    
    for word in s.split(" "):
        for i,s in enumerate(word):
            if i%2 == 0: answer+=s.upper()
            else: answer+=s.lower()
        answer +=' '
    return answer[:-1]