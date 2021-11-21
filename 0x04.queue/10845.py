# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline


li = []
front = 0
rear = 0

for _ in range(int(input())):
    c = input().split()

    if c[0] == 'push':
        li.append(c[1])
        rear +=1
    elif c[0] == 'pop':
        if front == rear: print('-1')
        else:
            print(li[front])
            front +=1
    elif c[0] == 'size':
        print(rear-front)
    elif c[0] == 'empty':
        if rear == front: print('1')
        else: print('0')
    elif c[0] == 'front':
        if front == rear: print('-1')
        else: print(li[front])
    else:
        if front == rear: print('-1')
        else: print(li[rear-1])