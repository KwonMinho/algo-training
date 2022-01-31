def solution(string):
    answer = True
    
    stack = []
    
    for s in string:
        if stack and s != stack[-1]:
            stack.pop()
        else:
            if not stack and s == ')':
                return False
            stack.append(s)
            
    print(stack)
    if stack: return False
    else: return True