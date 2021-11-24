# 재귀적 사고
# a^50 mod 6이 N이라면
# a^100 mod 6은 N*N

A, B, C = map(int, input().split())

def pow(a, b, m):
    if b == 1: return a%m
    val = pow(a, b//2, m)
    val = val*val%m
    if b % 2 == 0: return val
    return val * a % m

print(pow(A,B,C))