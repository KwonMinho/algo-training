import sys
input = sys.stdin.readline

N = int(input())
paper = [ list(map(int,input().split())) for _ in range(N)]
cnt = [0,0]

def check(x,y,n):
    global paper
    for i in range(x,n+x):
        for j in range(y,n+y):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def f(x,y,n):
    global paper
    if check(x,y,n):
        cnt[paper[x][y]] +=1
        return

    n=n//2
    for i in range(2):
        for j in range(2):
            f(x+i*n,y+j*n,n)


f(0,0,N)
for c in cnt:
    print(c)