N = int(input())


board = [ [" "]*N for _ in range(N)]



def f(x,y,n):
    global board

    if n==1:
        board[x][y] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue

            f(x+n//3*i, y+n//3*j, n//3)

f(0,0,N)

for row in board:
    print(''.join(row))