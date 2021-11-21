import sys
input = sys.stdin.readline

li = []
front = 0
rear = 0


N = int(input())


for i in range(1, N+1):
    if N==1: break
    li.append(i)
    rear +=1

i = 1
while True:
    if N==1:
        print(N)
        break
    if i%2 ==0:
        li.append(li[front])
        rear+=1

    front +=1

    if rear-front==1:
        print(li[front])
        break

    i+=1