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

print((1<<N)-1)
h(1,3,N)
