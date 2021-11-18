from sys import stdin

N = int(stdin.readline().rstrip())

li = []

for _ in range(N):
    cur = int(stdin.readline().rstrip())
    if cur ==0 and li:
        li.pop()
    else:
        li.append(cur)

print(sum(li))
