from sys import stdin

#left 끝에 있는 녀석이 커서
left = list(stdin.readline().rstrip())
right = []

for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())

    if command[0] == 'L':
        if left:
            right.append(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])

left.extend(reversed(right))
print(''.join(left))
