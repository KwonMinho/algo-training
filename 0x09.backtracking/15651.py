N, M = map(int, input().split())
arr = ['']*M

def solve(n):
    if n == M:
        for i in range(M):
            print(arr[i], end = ' ')
        print()
        return

    for i in range(N):
        arr[n] = str(i+1)
        solve(n+1)

solve(0)