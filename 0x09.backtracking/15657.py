N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))
arr = [''] * M

def solve(n,cur):
    if n == M:
        print(' '.join(arr).strip())
        return

    for i in range(cur,N):
        arr[n] = str(li[i])
        solve(n+1,i)

solve(0,0)
