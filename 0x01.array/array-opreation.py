
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34]


def insert(index, num, arr):
    if len(arr) > index:
        for i in range(index, len(arr)):
            num, arr[i] = arr[i], num

    arr.append(num)


def erase(index, arr):
    length = len(arr)
    if length-1 < index or index < 0:
        print("bound out of error")
        return

    if length > index:
        for i in range(index+1, length):
            arr[i-1] = arr[i]

    del arr[length-1]


print(arr)
insert(5, 999, arr)
print(arr)
