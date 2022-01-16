def solution(id_list, report, k):
    answer = []
    
    reported_users = {}
    u_index = {}
    
    for i,id in enumerate(id_list):
        reported_users[id] = []
        u_index[id] = i
        answer.append(0)
    
    for r in report:
        user, target = r.split()
        reported_users[target].append(user)
    
    for target in reported_users:
        users = set(reported_users[target])
        if len(users) < k: continue
        for user in users:
            answer[u_index[user]] +=1
           
    return answer