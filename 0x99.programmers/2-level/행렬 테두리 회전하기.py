def solution(rs, cs, queries):
    answer = []
    
    board = [[ r*cs+c+1 for c in range(cs)] for r in range(rs)]

    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1

        start = board[top][left]
        m = start
        
        for y in range(top, bottom):
            board[y][left] = board[y+1][left]
            m = min(m, board[y][left])
        
        for x in range(left, right):
            board[bottom][x] = board[bottom][x+1]
            m = min(m, board[bottom][x])
        
        for y in range(bottom, top, -1):
            board[y][right] = board[y-1][right]
            m = min(m, board[y][right])
            
        for x in range(right, left, -1):
            board[top][x] = board[top][x-1]
            m = min(m, board[top][x])
            
        board[top][left+1] = start
        answer.append(m)
    
    return answer