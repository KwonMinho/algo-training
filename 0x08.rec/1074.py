N,R,C = map(int,input().split())

def re(n,r,c):
    if n==0: return 0

    half = 1<<(n-1)
    if r < half and c < half:
        return re(n-1,r,c)
    elif r < half and c >=half:
        return half*half + re(n-1, r, c-half)
    elif r >= half and c < half:
        return 2*half*half+ re(n-1, r-half, c)
    else:
        return 3*half*half+ re(n-1, r-half, c-half)

print(re(N,R,C))

# tmp=(2**N)
# i = tmp-1
# print(tmp, i,i)
# fibo((tmp*tmp)-1,i,i)