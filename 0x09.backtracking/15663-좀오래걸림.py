N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))
visited = [False] * N
arr = [''] * N

def solve(n):
    if n == M:
        print(' '.join(arr).strip())
        return

    tmp = []
    for i in range(N):
        if li[i] in tmp or visited[i]:
            continue
        visited[i] = True
        tmp.append(li[i])
        arr[n] = str(li[i])
        solve(n+1)
        visited[i] = False

solve(0)
