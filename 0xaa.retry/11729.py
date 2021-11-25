N = int(input())


def h(a, b, n):
    global cnt
    if n==1:
        print(a,b)
        return
    else:
        h(a, 6-a-b, n-1)
        print(a,b)
        h(6-a-b,b,n-1)

# 2^N == 1<<N (1을 비트 기준으로 N칸 밀어라)
print((1<<N)-1)
h(1,3,N)
