import sys
input = sys.stdin.readline

while True:
    line=input()[:-1]
    if line == '.': break

    stack = []
    ans = 'yes'
    for s in line:
        if s=='[' or s =='{' or s == '(':
            stack.append(s)
        elif s==']':
            if len(stack)==0 or stack.pop()!='[':
                ans = 'no'
                break
        elif s=='}':
            if len(stack)==0 or stack.pop()!='{':
                ans = 'no'
                break
        elif s==')':
            if len(stack)==0 or stack.pop()!='(':
                ans = 'no'
                break

    if len(stack)!=0: ans='no'
    print(ans)