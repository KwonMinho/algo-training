ys, xs = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(ys)]
board2 = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cctv = []
all = 0
mini = 11111111


def upd(x, y, dir):
    dir %= 4  # 추출
    cnt = 0
    while True:
        x += dx[dir]
        y += dy[dir]
        if isOverBoundary(x, y) or board2[y][x] == 6:
            return cnt
        if board2[y][x] != 0 or board2[y][x] == 7:
            continue
        board2[y][x] = 7
        cnt += 1


def isOverBoundary(x, y):
    return x < 0 or x >= xs or y < 0 or y >= ys


for y in range(ys):
    for x in range(xs):
        if board[y][x] != 6 and board[y][x] != 0:
            cctv.append((y, x))
        if board[y][x] == 0:
            all += 1


for tmp in range(4**len(cctv)):
    board2 = [x[:] for x in board]

    cnt = 0
    for i in range(len(cctv)):
        dir = int(tmp % 4)
        tmp /= 4
        y, x = cctv[i]

        if board[y][x] == 1:
            cnt += upd(x, y, dir)
        elif board[y][x] == 2:
            cnt += upd(x, y, dir)
            cnt += upd(x, y, dir+2)
        elif board[y][x] == 3:
            cnt += upd(x, y, dir)
            cnt += upd(x, y, dir+1)
        elif board[y][x] == 4:
            cnt += upd(x, y, dir)
            cnt += upd(x, y, dir+1)
            cnt += upd(x, y, dir+2)
        elif board[y][x] == 5:
            cnt += upd(x, y, dir)
            cnt += upd(x, y, dir+1)
            cnt += upd(x, y, dir+2)
            cnt += upd(x, y, dir+3)

    mini = min(mini, all-cnt)


print(mini)
