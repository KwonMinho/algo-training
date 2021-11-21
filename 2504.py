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