#15649-others
n, m = map(int, input().split())

ans = ['0']*n
visited = [False]*n ##core

def f(k):
    global n,m
    if k==m:
        print(" ".join(ans[0:m]))
        return

    for i in range(0,n):
        if not visited[i]:
            visited[i] = True ## core!
            ans[k] = str(i+1)
            f(k+1)
            visited[i] = False ## core!
f(0)