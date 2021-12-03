N, M = map(int, input().split())

arr = [-1]*N
visited = [False]*N

def solve(n):
    if n==M:
        res = ""
        for i in range(N):
            if visited[i]:
                res+=str(i+1)+" "
        print(res[:-1])
        return

    st = 0
    if n!=0: st = arr[n-1]
    for i in range(st,N):
        if not visited[i]:
            arr[n] = i+1
            visited[i] = True
            solve(n+1)
            visited[i] = False

solve(0)