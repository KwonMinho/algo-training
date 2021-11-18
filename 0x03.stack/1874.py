from sys import stdin


N = int(stdin.readline().rstrip())
seq = [ int(stdin.readline().rstrip()) for _ in range(N)]
seq_top = 0

value = 1
stack = [value]
cursor = 1

res = []
is_pause = False


while seq_top < N:
    if stack[cursor-1] > seq[seq_top]:
        print('NO')
        is_pause = True
        break

    if value == seq[seq_top]:
        res.append('+')
        res.append('-')
        value+=1
        seq_top+=1
    elif stack[cursor-1] == seq[seq_top]:
        stack.pop()
        cursor -=1
        res.append('-')
        seq_top+=1
    else:
        stack.append(value)
        value+=1
        cursor +=1
        res.append('+')


if not is_pause:
    for v in res:
        print(v)