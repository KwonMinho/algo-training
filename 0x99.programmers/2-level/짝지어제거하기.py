def solution(s):
    arr = list(s)    
    prev_len = 0
    
    while prev_len != len(arr):
        prev_len = len(arr)
        
        stack = []
        cnt = len(arr)
        while cnt:
            cnt-=1
            cur = arr.pop()
            
            if stack and cur == stack[-1]:
                stack.pop()
            else:
                stack.append(cur)
                
        arr = stack[:]
        
    if arr: return 0
    else: return 1