from IPython.display import clear_output
def display_board(board):
    n=1
    loop=len(board)
    while loop>n:
        print(board[n],'|',board[n+1],'|',board[n+2])
        print('----------')
        n=n+3

def player_input():
    inp=' '
    while inp not in ['X','O']:
        print("Please enter your input as 'X' or 'O'")
        inp=input()

def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board,mark):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for item in win:
        n=0
        if (board[item[n]]==board[item[n+1]] and board[item[n+1]]==board[item[n+2]] and board[item[n+2]]==mark):
            flag=1
        else:
            flag=0
    if flag==1:
        return(True)
    else:
        return(False)
    
import random
def choose_first():
    global player1
    global player2
    choice=random.randint(1,2)
    if choice==1:
        player1='X'
        player2='O'
        print('Player X goes first')
    if choice==2:
        player1='O'
        player2='X'
        print('Player O goes first')
        
def space_check(board,position):
    if board[position] not in ['X','O']:
        return(True)
    else:
        return(False)
    
def full_board_check(board):
    for board_item in board:
        if board_item not in ['X','O','#']:
            full=False
            break
        else:
            full=True
    if full:
        return(True)
    else:
        return(False)
        
def player_choice(board):
    print('Enter the position you want to place your marker')
    position=input()
    space_check(board,position)
    
def replay(board):
    if(full_board_check(board)):
        print('Game Draw - Board Full')
    print('Do you want to play again?(yes/no)')
    replay=input()
    if replay=='yes':
        return(True)
    else:
        return(False)
    
def mainjob():
    print('Welcome to Tic Tac Toe!')
    print('Below is the board with positions indicated')
    test_board=['#','1','2','3','4','5','6','7','8','9']
    display_board(test_board)
    player_input()
    choose_first()
    board=test_board
    game_over=False
    #full_board=False
    #print(full_board_check(board))
    while not(full_board_check(board) or game_over):
        #print(full_board_check(board))
        #print('{} Game Over'.format(game_over())
        #Player 1 Turn
        print('Player 1 - Your turn')
        player1
        print('Please enter the position you want to place your marker')
        position=int(input())
        while not space_check(board,position):
            print('Position selected is not available, please choose an available position')
            position=int(input())
        if space_check(board,position):
            place_marker(board,player1,position)
            display_board(board)
        if win_check(board,player1):
            print('Player1 wins')
            game_over=True
        elif not(full_board_check(board) or game_over):
        # Player2's turn.
            print('Players 2 - Your turn')
            print('Please enter the position you want to place your marker')
            position=int(input())
            while not space_check(board,position):
                print('Position selected is not available, please choose an available position')
                position=int(input())
            if space_check(board,position):
                place_marker(board,player2,position)
                display_board(board)
            if win_check(board,player2):
                print('Player2 wins')  
                game_over=True
            #full_board=full_board_check(board)
                
    if not replay(board):
        print('Thank you')
    else:
        clear_output()
        mainjob()
mainjob()