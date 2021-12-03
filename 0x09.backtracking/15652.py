N, M = map(int, input().split())

visited = [False]*N
arr = ['']*N

def solve(n, prev):
    if n==M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return

    for i in range(prev, N):
        arr[n] = str(i+1)
        solve(n+1, i)

solve(0,0)