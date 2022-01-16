def solution(info, query):
    answer = []
    data = {}
    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        if (a,b,c,d) in data: 
                            data[(a, b, c, d)].append(int(i[4]))
                        else:
                            data[(a,b,c,d)] = [int(i[4])]
    
    for value in data.values():
        value.sort()
        
    for qr in query:
        q = qr.split()
        score = int(q.pop())
        key = (q[0], q[2], q[4], q[6])
        
        if key in data:
            pass
            scores = data[key]
            l, r = 0, len(scores)
            while l < r:
                mid = (l+r)//2
                if scores[mid] >= score:
                    r = mid
                else:
                    l = mid+1
            answer.append(len(scores)-l)
        else:
            answer.append(0)

    return answer