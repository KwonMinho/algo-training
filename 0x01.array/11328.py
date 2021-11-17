# https://www.acmicpc.net/problem/11328

M = int(input())
str_set = [tuple(map(str, input().split())) for _ in range(M)]

for (str1, str2) in str_set:
    ls = [0]*26
    isPossible = True

    for s1, s2 in zip(str1, str2):
        ls[ord(s1)-97] += 1
        ls[ord(s2)-97] -= 1

    for v in ls:
        if v != 0:
            isPossible = False
            break

    if isPossible:
        print("Possible")
    else:
        print("Impossible")
