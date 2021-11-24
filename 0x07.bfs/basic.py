from collections import deque

N, M = 100,100
board = [ [0]*M for _ in range(N)]
vis = [ [False]*M for _ in range(N)]
q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

vis[0][0] = True
q.appendleft((0,0))


while q:
    x,y=q.pop()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if vis[nx][ny] or board[nx][ny]!=1: continue

        vis[nx][ny] = True
        q.append((nx,ny))

