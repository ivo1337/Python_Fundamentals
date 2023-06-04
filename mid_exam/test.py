board = [' ' for _ in range(9)]

def print_board():
    print(' | ', board[0], ' | ', board[1], ' | ', board[2], ' | ')
    print(' | ', board[3], ' | ', board[4], ' | ', board[5], ' | ')
    print(' | ', board[6], ' | ', board[7], ' | ', board[8], ' | ')

def play_game():
    current_player = 'X'
    game_over = False
    while not game_over:
        print_board()
        position = int(input('Choose a position from 1-9: '))
        if board[position-1] == ' ':
            board[position-1] = current_player
            if check_win():
                print_board()
                print('Game Over! ' + current_player + ' wins!')
                game_over = True
            elif check_tie():
                print_board()
                print('Game Over! It\'s a tie!')
                game_over = True
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        else:
            print('That position is already taken!')

def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def check_tie():
    if all(i != ' ' for i in board):
        return True
    return False

play_game()