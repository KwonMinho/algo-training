visited = [False]*20

def solve(n, cur, li):
    if n == 6:
        for i in range(len(li)):
            if visited[i]:
                print(str(li[i]),end=' ')
        print()
        return

    for i in range(cur, len(li)):
        if visited[i]: continue

        visited[i] = True
        solve(n+1, i, li)
        visited[i] = False


while True:
    li = list(map(int, input().split()))
    if li[0] == 0: break
    del li[0]
    solve(0, 0, sorted(li))
    print()
