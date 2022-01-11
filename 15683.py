import sys
input = sys.stdin.readline
from copy import deepcopy


def oob(x,y):
    return x < 0 or x >= N or y < 0 or y>= M

def upd(x,y,dir,board2):
    dir %=4
    while True:
        x += dx[dir]
        y += dy[dir]
        if oob(x,y) or board2[x][y] == 6: return
        if board2[x][y] != 0: continue
        board2[x][y] = 7

N, M= map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
mn = 0
cctvs = []
directions = []

for x in range(N):
    line = list(map(int,input().split()))
    for y,obj in enumerate(line):
        if obj != 0 and obj !=6:
            cctvs.append((obj,x,y)) #type,x,y
        else: mn+=1
    board.append(line)


for tmp in range(4*len(cctvs)):
    board2 = deepcopy(board)

    for cctv in cctvs:
        dir = tmp%4
        tmp //=4
        type,x,y = cctv

        if type == 1:
            upd(x,y,dir,board2)
        elif type == 2:
            upd(x,y,dir,board2)
            upd(x,y,dir+2,board2)         
        elif type == 3:
            upd(x,y,dir,board2)
            upd(x,y,dir+1,board2)
        elif type == 4:
            upd(x,y,dir,board2)
            upd(x,y,dir+1,board2)
            upd(x,y,dir+2,board2)
        else:
            upd(x,y,dir,board2)
            upd(x,y,dir+1,board2)
            upd(x,y,dir+2,board2)
            upd(x,y,dir+3,board2)

    cnt = 0
    for line in board2:
        cnt += line.count(0)
    mn = min(mn, cnt)

print(mn)