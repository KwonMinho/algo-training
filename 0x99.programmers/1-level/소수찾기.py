import math

prime_list = []

def isPrime(n):
    x=int(math.sqrt(n))
    
    if n<10:
        if n in [2,3,5,7]: return True
        else: return False
    
    for p in prime_list:
        if p > x: 
            break
        if n%p == 0: 
            return False
    return True
            

def solution(n):
    answer = 0
    
    for num in range(2,n+1):
        if isPrime(num):
            prime_list.append(num)
            answer+=1
    return answer