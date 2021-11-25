import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int,input().split())) for _ in range(N)]
cnt = [0,0,0]

def check(x, y, n):
    global paper

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True


def solve(x, y, z):
    global cnt

    if check(x, y, z):
        cnt[paper[x][y]+1] +=1
        return

    n = z//3
    for i in range(0,3):
        for j in range(0,3):
            solve(x+i*n, y+j*n, n)


solve(0,0,N)
for i in cnt:
    print(i)