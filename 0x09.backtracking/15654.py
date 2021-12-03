N, M = map(int, input().split())
li = sorted(list(map(int,input().split())))

arr = ['']*N
visited = [False]*N

def solve(n):
    if n==M:
        print(' '.join(map(str, arr)).strip())
        return

    for i in range(N):
        if visited[i]: continue
        arr[n] = str(li[i])
        visited[i] = True
        solve(n+1)
        visited[i] = False

solve(0)
