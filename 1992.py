import sys
input = sys.stdin.readline

N = int(input())
paper = [list(input().rstrip()) for _ in range(N)]
res = ''

def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def f(x,y,n):
    global res, paper
    if check(x,y,n):
        res+= paper[x][y]
        return

    n = n//2
    res += '('
    for i in range(2):
        for j in range(2):
            f(x+i*n, y+j*n, n)

    res += ')'



f(0,0,N)
print(res)