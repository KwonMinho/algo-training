# https://hooongs.tistory.com/330

import sys
input = sys.stdin.readline

n,*l=[1,2,3,4,4]


while True:
    n,*line = list(map(int, input().split()))

    if n==0: break

    s = []
    answer = 0

    # s[-1]: 작은 height의 인덱스
    for i in range(n):
        while s and line[s[-1]] > line[i]:
            prev_index = s.pop()

            if len(s) ==0: width = i
            else: width = i-stat

