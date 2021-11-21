import sys
input = sys.stdin.readline
MAX = 100000

N = int(input())

d = ['-1']*MAX

front = int(MAX/2)
rear = int(MAX/2)+1

while N>0:
    c = input().split()

    if c[0]=='push_front':
        #정수 X를 덱의 앞에 넣는다.
        d[front] = c[1]
        front-=1
    elif c[0] =='push_back':
        # 정수 X를 덱의 뒤에 넣는다.
        d[rear] = c[1]
        rear+=1
    elif c[0] =='pop_front':
        if rear-front==1: print('-1')
        else:
            front+=1
            print(d[front])
    #덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'pop_back':
    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if rear-front==1: print('-1')
        else:
            rear-=1
            print(d[rear])
    elif c[0] == 'size':
        print(rear-front-1)
        # 덱에 들어있는 정수의 개수를 출력한다.
    elif c[0] == 'empty':
        if rear-front==1: print('1')
        else: print('0')
       # 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif c[0] == 'front':
        if rear-front==1: print('-1')
        else:
            print(d[front+1])
        # 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'back':
        if rear-front==1: print('-1')
        else:
            print(d[rear-1])

    N-=1
        # 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.