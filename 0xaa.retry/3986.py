import sys
input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    line = input().strip()
    stack = []

    for s in line:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

    if not stack: cnt+=1

print(cnt)