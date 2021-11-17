def conversion(target, n):

    digit = 1
    value = 0
    while target > 0:
        value += int(target%n)*digit
        target = target/n
        digit*=10

    return value

def conversion_ten(target, n):
    digit = 1
    value = 0
    while target > 0:
        value += (int(target)%n)*n**(digit-1)
        target = target/10
        digit+=1
    return value

1373번 :  www.acmicpc.net/problem/1373
1212번 : www.acmicpc.net/problem/1212
11005번 : www.acmicpc.net/problem/11005
2745번 : www.acmicpc.net/problem/2745
11576번 : www.acmicpc.net/problem/11576
""
def bin2Hex(bin):

    while bin > 0:
        len = 0
        value = 0
        for digit in range(4):
            if bin/10 ==0: break

            value+=int(bin%2)*(2**digit)
            len+=1


print(conversion(50,5))
print(conversion_ten(200,5))
