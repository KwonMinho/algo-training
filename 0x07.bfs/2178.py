import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N, M = map(int,input().split())
board = [ input().rstrip() for _ in range(N)]
dis = [[-1]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

dis[0][0] = 1
q.appendleft((0,0))


while q:
    x,y=q.pop()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if dis[nx][ny] != -1 or board[nx][ny] != '1': continue

        dis[nx][ny] = dis[x][y]+1
        q.appendleft((nx,ny))

print(dis[N-1][M-1])