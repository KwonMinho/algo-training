# 1. case ' ( '
#    temp에 2를 곱하고 스택에 ' ( ' 를 push

# 2. case ' ) '
#    1) 스택이 비어있거나 스택 top이 ' ( ' 가 아닌 경우
#    올바르지 못한 괄호열이므로 answer = 0; break;

#    2) 이전 문자열이 ' ( ' 일 경우
#    괄호 값이 '( )' 이므로 계산된 temp 값을 answer에 더해주고 temp를 2로 나눈다. 스택을 pop 한다.

#    3) 이전 문자열이 ' ( ' 가 아닐 경우 ==> !!!!!!!!!! ex) (())!!!!!!!!
#    제일 안쪽 괄호, 즉 '( )' 형태가 아니므로 이미 answer에 값이 더해져 있는 상태이다. 따라서 answer에 값을 더하지 않고 temp를 2로 나누고 스택 pop을 한다. 



import sys
input = sys.stdin.readline

line = input()
sum = 0
stack = []
value = 1
for i in range(len(line)):
    if line[i] == '(':
        value *=2
        stack.append(line[i])
    elif line[i] == '[':
        value *=3
        stack.append(line[i])
    elif line[i] == ')':
        if not stack or stack[-1] != '(':
            sum = 0
            break
        if line[i-1] == '(':
            sum += value
        stack.pop()
        value //=2
    elif line[i] == ']':
        if not stack or stack[-1] != '[':
            sum = 0
            break

        if line[i-1] == '[':
            sum +=value
        stack.pop()
        value //=3


if stack: sum = 0

print(sum)