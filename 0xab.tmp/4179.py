from collections import deque


rows, cols = map(int, input().split())
board = [list(map(str, input())) for _ in range(rows)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
fire_q = deque()
ans = []


for r in range(rows):
    for c in range(cols):
        if board[r][c] == '#' or board[r][c] == '.':
            continue

        if board[r][c] == 'J':
            if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                ans.append(1)
                break
            q.append((r, c, 1))
        elif board[r][c] == 'F':
            fire_q.append((r, c, 1))


while fire_q:
    x, y, time = fire_q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            continue
        if board[nx][ny] != '.' and board[nx][ny] != 'J':
            continue

        board[nx][ny] = str(time+1)
        fire_q.append((nx, ny, time+1))


while q:
    x, y, time = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            continue
        if board[nx][ny] == '#' or board[nx][ny] == 'F' or board[nx][ny] == 'J':
            continue
        if board[nx][ny] != '.' and int(board[nx][ny]) <= time+1:
            continue
        if nx == 0 or ny == 0 or nx == rows-1 or ny == cols-1:
            ans.append(time+1)
            continue

        q.append((nx, ny, time+1))
        board[nx][ny] = 'J'


if len(ans) == 0:
    print("IMPOSSIBLE")
else:
    print(min(ans))
