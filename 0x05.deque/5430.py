import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ops = input().rstrip()
    n = int(input().rstrip())
    arr = input().rstrip()

    if n==0: arr=[]
    else: arr = arr[1:-1].split(',')

    front= 0
    rear= len(arr)
    is_reverse = False

    for op in ops:
        if op == 'R':
            if not is_reverse:
                front,rear = rear-1,front-1
            else:
                front,rear = rear+1,front+1
            is_reverse = not is_reverse
        else:
            if abs(front-rear)==0:
                front='x'
                break
            else:
                if is_reverse: front-=1
                else: front+=1

    if front == 'x': print('error')
    else:
        dir = 1
        if is_reverse: dir =-1

        res ='['
        while abs(front-rear)>1:
            res+=arr[front]+','
            front+=dir

        if abs(front-rear)!=0: res+=arr[front]
        print(res+']')