import sys
input = sys.stdin.readline

for _ in range(int(input())):
    st = input()

    stack = []
    is_yes = True
    for s in st:
        if s == '(':
            stack.append(s)
        elif s ==')':
            if not stack or '(' != stack.pop():
                is_yes = False
                break

    if stack or not is_yes: print("NO")
    else: print("YES")

