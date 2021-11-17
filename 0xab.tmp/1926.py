from collections import deque

rows,cols = map(int, input().split())
board = [ list(map(int,input().split())) for _ in range(rows) ]
vis = [ [False]*cols for _ in range(rows) ] #열이 복사 [[False]*cols]*rows
dx = [1,0,-1,0]
dy = [0,1,0,-1]

max_area = 0
draw_cnt = 0

for i in range(0, rows):
    for j in range(0, cols):
        if vis[i][j] or board[i][j] == 0: continue

        q = deque()
        vis[i][j] = True
        q.append((i,j))
        draw_cnt +=1
        area = 0

        while q:
            area+=1
            cur_x, cur_y = q.pop()

            for d in range(0,4):
                nx = cur_x + dx[d]
                ny = cur_y + dy[d]

                if nx<0 or ny<0 or nx>=rows or ny>=cols: continue
                if vis[nx][ny] or board[nx][ny] != 1: continue
                vis[nx][ny] = True
                q.append((nx,ny))

        max_area = max(area,max_area)

print(draw_cnt)
print(max_area)