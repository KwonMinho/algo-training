N, M = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
a,b = 0,0

answer = []

while True:
  if a >= N:
    answer = answer+arr_b[b:]
    break
  
  if b >= M:
    answer = answer+arr_a[a:]
    break

  if arr_a[a] > arr_b[b]:
    answer.append(arr_b[b])
    b+=1
  else:
    answer.append(arr_a[a])
    a+=1

print(' '.join(list(map(str,answer))))