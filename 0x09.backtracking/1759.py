L, C = map(int, input().split())
li = sorted(list(map(str, input().split())))

visited = [False]*C
def solve(n,cur):
    if n == L:
        res = ''
        vowels=not_vowels=0
        for i in range(C):
            if not visited[i]: continue

            if li[i] in ('a','e','i','o','u'):
                vowels+=1
            else:
                not_vowels +=1

            res +=li[i]

        if res!='' and vowels>=1 and not_vowels>=2:
            print(res)
        return

    for i in range(cur,C):
        if visited[i]:
            continue

        visited[i] = True
        solve(n+1,i)
        visited[i] = False

solve(0,0)