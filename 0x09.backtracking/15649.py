N, M = map(int, input().split())

def solve(cnt, v, res):
    global N, M

    if cnt == M:
        print(res[:-1])

    for i in range(1, N+1):
        cur = str(i)
        if res.find(cur) != -1:
            continue

        solve(cnt+1, i, res+cur+" ")

solve(0, 0, '')