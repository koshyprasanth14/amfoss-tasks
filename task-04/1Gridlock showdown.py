def check_winner(board):
   
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return board[0][2]
    
    return 'DRAW'

def solve():
    t = int(input())
    for j in range(t):
        board = [list(input()) for j in range(3)] 
        result = check_winner(board)
        print(result)

solve()