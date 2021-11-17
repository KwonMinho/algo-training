from collections import deque

cols, rows = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(rows)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
for r in range(rows):
    for c in range(cols):
        if board[r][c] == 1:
            q.append((r, c))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            continue
        if board[nx][ny] != 0:
            continue
        board[nx][ny] = board[x][y]+1
        q.append((nx, ny))

ans = 1
noAns = False

for r in range(rows):
    for c in range(cols):
        cur = board[r][c]
        if cur == 0:
            ans = 0
            break
        ans = max(ans, cur)
    if ans == 0:
        break

print(ans-1)
