# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


from sys import stdin

n = int(stdin.readline().rstrip())

top = 0
li = []

for _ in range(n):
    v = stdin.readline().rstrip().split()

    if v[0] =='push':
        li.append(v[1])
        top +=1
    elif v[0] == 'pop':
        if top == 0:
            print(-1)
        else:
            print(li.pop())
            top -=1
    elif v[0] == 'size':
        print(top)
    elif v[0] == 'empty':
        if top==0: print(1)
        else: print(0)
    else:
        if top==0: print(-1)
        else: print(li[top-1])

