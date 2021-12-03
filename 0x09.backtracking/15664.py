N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))

arr = [''] * N

def solve(n, cur):
    if n == M:
        print(' '.join(arr).strip())
        return

    tmp = []
    for i in range(cur, N):
        if li[i] in tmp:
            continue

        arr[n] = str(li[i])
        tmp.append(li[i])
        solve(n+1, i+1)

solve(0,0)