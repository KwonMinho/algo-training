N = int(input())
ls = list(map(int, input().split()))
target = int(input())
arr = [0]*250


for v in ls:
    arr[100+v] += 1


print(arr[100+target])

# print(arr[target])
