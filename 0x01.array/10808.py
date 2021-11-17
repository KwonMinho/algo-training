# 알파벳 개수
# -ord("a"): 아스키 값, chr(100): 아스키 코드
# - A(65), a(97)
# - 알파벳 26

value = input()


ls = [0]*26
for v in value:
    index = (ord(v)-97)
    ls[index] += 1

res = ''
for v in ls:
    res += str(v)+' '

print(res)
