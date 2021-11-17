value = int(input())

ls = [0]*10
mx = -1

while value > 0:
    index = int(value % 10)
    value = value//10

    ls[index] += 1

    cur = ls[index]
    if index == 6 or index == 9:
        cur = int((ls[6]+ls[9]+1)/2)

    mx = max(mx, cur)

print(mx)
