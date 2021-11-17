...
두 수의 합이 100이 되는 수가 있는지 없는지
...


value = [1, 52, 48]
arr = [0]*100


def func2(ls, arr):
    for v in ls:
        if arr[100-v] != 0:
            return 1
        arr[v] = 1

    return 0


print(func2(value, arr))
