N = int(input())
ans = [[' ']*2*N for _ in range(N)]


def make_star(x, y, n):
    ans[x][y] = "*"
    ans[x+1][y-1] = ans[x+1][y+1] = "*"
    for i in range(-2,3):
        ans[x+2][y+i] = "*"

def solve(x, y, n):
    if n == 3:
        make_star(x,y,n)
    else:
        n //=2
        solve(x, y, n)
        solve(x+n, y+n, n)
        solve(x+n, y-n, n)

solve(0, N-1, N)
for row in ans:
    print("".join(row))