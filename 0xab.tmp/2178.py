from collections import deque

rows, cols = map(int, input().split())
board = [list(map(int, input())) for _ in range(rows)]
dis = [[0]*cols for _ in range(rows)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

min_path = 0


q = deque()
q.append((0, 0))
dis[0][0] = 1
path_rank = []

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
            continue
        if dis[nx][ny] > 0 or board[nx][ny] != 1:
            continue
        q.append((nx, ny))
        dis[nx][ny] = dis[x][y]+1

print(dis[rows-1][cols-1])
