N, S  = map(int,input().split())
li =  [int(a) for a in input().split()]

cnt = 0

def solve(cur, t):
    global cnt
    if N == cur:
        if t ==  S: cnt+=1
        return
    solve(cur+1, t)
    solve(cur+1, t+li[cur])


solve(0, 0)
if S == 0: cnt-=1
print(cnt)