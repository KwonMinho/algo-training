### 꼭 다시 풀어보기 틀림 #### https://guru.tistory.com/27


## 같거나 작으면 pop
## 같다면 pop한 녀석의 이전 pop한 횟수를 더해줘야함
## 자기보다 큰게나오면 +1
import sys
input =sys.stdin.readline
r=0
s=[]
for _ in range(int(input())):
    b=int(input())
    x=1
    while s and s[-1][0] <=b:
        prev,num = s.pop()
        if prev == b:
            x+=num
        r+=num
    if s:
        r+=1
    s.append((b,x))

print(r)