str1 = input()
str2 = input()


a = [0]*1000
b = [0]*1000
res = 0

length = max(len(str1), len(str2))

for i in range(length):
    if i < len(str1):
        a[ord(str1[i])-97] += 1
    if i < len(str2):
        b[ord(str2[i])-97] += 1

for a1, b2 in zip(a, b):
    if a1 != b2:
        res += abs(a1-b2)


print(res)


# abbcccddddeeeee
# eddcccbbbbaaaaa

# abb
# ab
