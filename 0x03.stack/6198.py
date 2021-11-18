# 첫번째 푼 접근법
# 현재 빌딩 > 스택 체크 리스트에 탑에 있는 빌딩
# 1. 내보다 작은 빌딩의 수 = 현재 체크 빌딩이 가지고있던 빌딩의 수 + 1
# 2. 그리고 그 빌딩 pop)()
from sys import stdin

N = int(stdin.readline().rstrip())

building = []
check = []
for i in range(1,N+1):
    building.append([int(stdin.readline().rstrip()),0])

res = 0
while building:
    b = building.pop()
    c_len= len(check)-1
    views = 0
    while check:
        if b[0] > check[c_len][0]:
            b[1] +=1+check[c_len][1]
            check.pop()
            c_len-=1
        else:
            break
    res+=b[1]
    check.append(b)

print(res)


##-- 다른 사람 풀이 -- ##

# import sys

# N = int(sys.stdin.readline())
# li = [int(sys.stdin.readline()) for _ in range(N)]
# stack, res = [], 0
# for i in range(N):
#     while stack != [] and stack[-1] <= li[i]:
#         stack.pop()
#     stack.append(li[i])
#     res += len(stack)-1
# print(res)


## 두번째 빌딩
#  현재보는 빌딩 A를 볼 수 있는 이전 빌딩의 개수를 측정
#  A가 이전 빌딩보다 크다면 그 빌딩을 이전 빌딩에서 제외시킴 
# (왜냐하면 다음 빌딩이 나오더라도 제외시킨 빌딩은 현재 빌딩때문에 못보기때문에)
from sys import stdin

N = int(stdin.readline().rstrip())
prev = []
ans = 0
while N>0:
    N-=1

    h = int(stdin.readline().rstrip())
    while prev and prev[-1] <= h:
        prev.pop()
    ans+=len(prev)
    prev.append(h)

print(ans)
# int main() {
#   ios_base::sync_with_stdio(0);
#   cin.tie(0);

#   cin >> n;
#   ll h;
#   while (n--) {
#     cin >> h;
#     while(!s.empty() && s.top() <= h)
#       s.pop();
#     ans += s.size();
#     s.push(h);
#   }
#   cout << ans;
#   return 0;
# }


#  현재보는 빌딩 A를 볼 수 있는 이전 빌딩의 개수를 측정
#  A가 이전 빌딩보다 크다면 그 빌딩을 이전 빌딩에서 제외시킴 
# (왜냐하면 다음 빌딩이 나오더라도 제외시킨 빌딩은 현재 빌딩때문에 못보기때문에)
