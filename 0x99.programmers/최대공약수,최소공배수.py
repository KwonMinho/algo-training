# 두 수의 공통된 소인수를 모두 곱하면 최대공약수
# 두 수의 모든 소인수를 곱하면 최소 공배수
# https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95

# 유클리드 호제법
# 최대공약수: a%b = n -> b%n = n1 -> n%n1=n2 ... n1 이 0이 될때까지


def solution(n, m):
    answer = []
    
    a,b = max(n,m),min(n,m)
    
    # 최대공약수
    while b:
        c = a%b
        a = b
        b = c
    g = a
    answer.append(g)
    answer.append(n*m/g)
    
    return answer