from collections import deque

li = [list(input()) for _ in range(5)]
select = [False]*25
dx = [0,1,-1,0]
dy = [1,0,0,-1]
ans = 0


def check_adjacency():
    visit = [[False]*5 for _ in range(5)]
    select_2d  = [[False]*5 for _ in range(5)]
    q = deque()

    is_start = True
    for id in range(25):
        if select[id]:
            x, y = id//5, id%5
            select_2d[x][y] = True
            if is_start:
                visit[x][y] = True
                q.appendleft((x,y))
                is_start = False


    is_adjacency = False
    cnt = 1
    while q:
        x,y=q.pop()

        if cnt == 7:
            is_adjacency = True
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
            if not select_2d[nx][ny] or visit[nx][ny]: continue

            visit[nx][ny] = True
            q.appendleft((nx,ny))
            cnt+=1

    return is_adjacency


def more_than_four():

    cnt = 0
    for id in range(25):
        if not select[id]: continue
        x, y = id//5, id%5
        if li[x][y] == 'Y': cnt+=1
        if cnt == 4:
            return True

    return False


def combination(n, base):
    global ans

    if n==7:
        if not more_than_four() and check_adjacency():
            ans += 1
        return

    for i in range(base, 25):
        if select[i]: continue

        select[i] = True
        combination(n+1, i)
        select[i] = False




combination(0,0)
print(ans)


