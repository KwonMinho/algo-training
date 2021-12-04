
arr = [1,2,3,4,5]
M = 3
visit = [False]*5

def dfs(n, base):
    if n== M:
        for i in range(5):
            if not visit[i]: continue
            print(arr[i],end=" ")
        print()
        return

    for i in range(base,5):
        if visit[i]: continue

        visit[i] = True
        dfs(n+1, i)
        visit[i] = False


dfs(0,0)