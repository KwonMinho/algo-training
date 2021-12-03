
    # -: 가로열에 대해서 안해주는 이유는 x가 x+1 ㄷ되기때문에
    # I : y
    # / : x+y
    # ^/: x-y+N-1: x-y가 음수가 될수 있어서 해주는 것

N = int(input())
cnt = 0
v1 = [False]*40
v2 = [False]*40
v3 = [False]*40

def f(x):
    global N,cnt,v1,v2,v3
    if x == N:
        cnt+=1
        return

    for y in range(N):
        if v1[y] or v2[x+y] or v3[x-y+N-1]:
            continue
        v1[y] = True
        v2[x+y] = True
        v3[x-y+N-1] = True
        f(x+1)
        v1[y] = False
        v2[x+y] = False
        v3[x-y+N-1] = False

f(0)
print(cnt)
