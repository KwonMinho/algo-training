from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
li = stdin.readline().rstrip().split()

s=[]
ans = deque()

while li:
    num = int(li.pop())

    while s and num >= s[-1]:
        s.pop()

    if s:ans.appendleft(str(s[-1]))
    else:ans.appendleft('-1')

    s.append(num)


print(' '.join(ans))