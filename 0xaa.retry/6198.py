# 빌딩이 스택 체크리스트 안에 있는 빌딩 날려버릴때
# 날려버릴 빌딩이 이전에 날려버린 빌딩 값 플러스 + 현재 날가라는 빌딩 해서 현재 빌디에 넣어줌


from sys import stdin

N = int(stdin.readline().rstrip())

building = []
check = []
for i in range(1,N+1):
    building.append([int(stdin.readline().rstrip()),0])

res = 0
while building:
    b = building.pop()
    c_len= len(check)-1
    views = 0
    while check:
        if b[0] > check[c_len][0]:
            b[1] +=1+check[c_len][1]
            check.pop()
            c_len-=1
        else:
            break
    res+=b[1]
    check.append(b)

print(res)