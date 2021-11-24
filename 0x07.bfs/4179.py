import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

f_q = deque()
j_q = deque()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = []
j_vis = [[False]*M for _ in range(N)]

ex_time = 9999

for i in range(N):
    row = []
    for j,s in enumerate(input().rstrip()):
        if s == 'F': f_q.appendleft((i,j,0))
        if s == 'J': 
            j_q.appendleft((i,j,0))
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                ex_time = 0
        row.append(s)
    board.append(row)


while f_q and ex_time != 0:
    x,y,time=f_q.pop()
    next_time = int(time)+1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny] != '.': continue
        board[nx][ny] = str(next_time)
        f_q.appendleft((nx,ny,next_time))

while j_q and ex_time != 0:
    x,y,time=j_q.pop()
    next_time = int(time)+1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if j_vis[nx][ny] or board[nx][ny] == 'F' or board[nx][ny] == 'J' or board[nx][ny] == '#'  : continue
        if board[nx][ny] != '.' and int(board[nx][ny]) <= next_time: continue

        j_vis[nx][ny] = True
        j_q.appendleft((nx,ny,next_time))
        if nx == 0 or nx == N-1 or ny == 0 or ny == M-1:
            ex_time = min(ex_time,next_time)


if ex_time == 9999: print("IMPOSSIBLE")
else: print(ex_time+1)

