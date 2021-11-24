import sys
from collections import deque
input = sys.stdin.readline

q = deque()
M, N = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            q.appendleft((x,y))


while q:
    x,y = q.pop()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if board[nx][ny] != 0: continue

        board[nx][ny] = board[x][y]+1
        q.appendleft((nx,ny))


v = 1
for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            v = 0
            break

        v = max(v, board[x][y])

    if v==0: break

print(v-1)
