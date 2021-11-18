#맨 앞에 탑부터 체크리스트에 넣으면서 비교

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
tops = deque(stdin.readline().rstrip().split())
check = []

res = ''
index = 0
while tops:
    cur_top = int(tops.popleft())

    l = len(check)-1
    cnt = 0
    while check:
        if check[l][0] <= cur_top:
            check.pop()
            l-=1
        else:
            cnt = check[l][1]
            break

    index+=1
    check.append((cur_top, index))
    res += ' '+str(cnt)

print(res.lstrip())
