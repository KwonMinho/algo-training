# 백스페이스  '-'
# < > 화살표 +1,-1 움직일수 있다면



from sys import stdin


res = []

for _ in range(int(stdin.readline().rstrip())):
    string = list(stdin.readline().rstrip())
    left = list()
    right = list()

    for s in string:
        if s=='<':
            if left:
                right.append(left.pop())
        elif s=='>':
            if right:
                left.append(right.pop())
        elif s=='-':
            if left:
                left.pop()
        else:
            left.append(s)

    left.extend(reversed(right))
    res.append(''.join(left))

for r in res:
    print(r)
