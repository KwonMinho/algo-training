N, K = map(int, input().split())
li = sorted(list(map(int, input().split())))
arr = ['']*N

def solve(n,cur):
    if n == K:
        print(' '.join(map(str, arr)).strip())
        return

    for i in range(cur,N):
        arr[n] = str(li[i])
        solve(n+1,i+1)

solve(0,0)