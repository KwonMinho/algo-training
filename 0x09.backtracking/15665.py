N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))
arr = ['']*M

def solve(n):
    if n == M:
        print(' '.join(arr).strip())
        return

    tmp = []
    for i in range(N):
        if li[i] in tmp: continue

        tmp.append(li[i])
        arr[n] = str(li[i])
        solve(n+1)

solve(0)