from collections import deque

N, K = map(int,input().split())
arr = [-1]*100001

q = deque()

arr[N] = 0
q.appendleft(N)

while arr[K]==-1:
    x = q.pop()
    for nx in [x+1,x-1,x*2]:
        if nx < 0 or nx>100000: continue
        if arr[nx] != -1: continue
        arr[nx] = arr[x] + 1
        q.appendleft(nx)

print(arr[K])