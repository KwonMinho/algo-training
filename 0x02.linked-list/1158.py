#요세푸스 문제
#원형 큐

from sys import stdin
from collections import deque

N, K = map(int,input().split())


q = deque()

for i in range(N):
    q.append(i+1)


i = 1
res = '<'
cursor = K-1

while True:
    res += str(q[cursor])
    del q[cursor]
    if N-i == 0: break

    cursor = (cursor+K-1)%(N-i)
    i+=1
    res += ', '
    #(cursor+K)%(N-1)

res += '>'
print(res)