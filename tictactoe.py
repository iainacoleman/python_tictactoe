#Tic Tac Toe Game
# Iain Coleman April 2017

board_log = [0,0,0,0,0,0,0,0,0]
display_square = ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
sq_blank ="[ ]"
sq_player1 = "[O]"
sq_player2 = "[X]"
move_counter = 0

game_is_over = False


isPlayerOneTurn = True
its_a_draw = None


def display_game_board():
    
    global row_one
    global row_two
    global row_three
    
    global row_one_log
    global row_two_log
    global row_three_log
    
    global move
    global board_log
    
    row_one_log = [board_log[0], board_log[1], board_log[2]]
    row_two_log = [board_log[3], board_log[4], board_log[5]]
    row_three_log = [board_log[6], board_log[7], board_log[8]]
 
    row_one = display_square[0] + display_square[1] + display_square[2] 
    row_two = display_square[3] + display_square[4] + display_square[5]
    row_three = display_square[6] + display_square[7] + display_square[8]
    
    print(row_one)
    print(row_two)
    print(row_three)
    
    
def get_player_names():
    global player1
    player1 = input("Player 1 enter your name:  ")
    global player2 
    player2 = input("Player 2 enter your name:  ")
        
    
def player_one_turn():
    
    global move
    global board_log
    global display_square
    
    print(player1, "which square would you like?")
    move = int(input())
    
    while board_log[move-1]!= 0:
        move = int(input("Sorry, that square is taken. Which square would you like?  "))
    else:
        pass
        
    board_log[move-1] = 1
    display_square[move-1] = "[O]"
    print("Thanks,", player1)
    display_game_board()
    check_for_winner()
        
def player_two_turn():
    
    global move
    global move_counter
    global board_log
    global display_square
    
    print(player2, "which square would you like?")
    move = int(input())
    
    
    while board_log[move-1]!= 0:
        move = int(input("Sorry, that square is taken. Which square would you like?  "))
    else:
        pass
        
    board_log[move-1] = 2
    display_square[move-1] = "[X]"
    print("Thanks,", player2)
    display_game_board()
    check_for_winner()
    move_counter += 1

        
def check_for_winner():
    
    global player_one_has_won
    global its_a_draw
    
    #Horizontal Winning Conditions
    hor_p1_winner = sq_player1+sq_player1+sq_player1
    hor_p2_winner = sq_player2+sq_player2+sq_player2
    if row_one ==  hor_p1_winner or row_two == hor_p1_winner or row_three == hor_p1_winner:
        player_one_has_won = True
        game_is_over = True
        game_over()
    elif row_one ==  hor_p2_winner or row_two == hor_p2_winner or row_three == hor_p2_winner:    
        player_one_has_won = False
        game_is_over = True
        game_over()
    else:
        pass
    
    #Vertical Winning Conditions
    if (board_log[0] == 1 and board_log[3] == 1 and board_log[6] ==1) or (board_log[1] == 1 and board_log[4] == 1 and board_log[7] ==1) or (board_log[2] == 1 and board_log[5] == 1 and board_log[8] ==1): 
        player_one_has_won = True
        game_is_over = True
        game_over()
    elif (board_log[0] == 2 and board_log[3] == 2 and board_log[6] == 2) or (board_log[1] == 2 and board_log[4] == 2 and board_log[7] == 2) or (board_log[2] == 2 and board_log[5] == 2 and board_log[8] ==2):
        player_one_has_won = False
        game_is_over = True
        game_over()
    else:
        pass
        
    #Diagonal Winning Conditions   
    if (board_log[0] == 1 and board_log[4] == 1 and board_log[8] == 1) or (board_log[2] == 1 and board_log[4] == 1 and board_log[6] == 1):
        player_one_has_won = True
        game_is_over = True
        game_over()
    elif (board_log[0] == 2 and board_log[4] == 2 and board_log[8] == 2) or (board_log[2] == 2 and board_log[4] == 2 and board_log[6] == 2):
        player_one_has_won = False
        game_is_over = True
        game_over()
    else:
        pass
    
    #Draw conditions
    
    if move_counter >= 4:
        its_a_draw = True
        
    
    
def game_over():
    
    global its_a_draw
    global player_one_has_won
    
    if its_a_draw == True:
        print("It's a draw!")
    
    else:
        if player_one_has_won == True:
            print(player1,"has won!")
        else:
            print(player2,"has won!")
        
    play_again_var = input("Play again? (y/n)   ")
    
    if play_again_var == "y":
        restart_game()
    else:
        start_game()

def reset_board():
    global display_square
    global board_log
    global player_one_has_won
    global its_a_draw
    global move_counter
    
    move_counter = 0
    player_one_has_won = None
    its_a_draw = None
    display_square = ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
    board_log = [0,0,0,0,0,0,0,0,0]

def start_game():
    
    global game_is_over
    
    reset_board()
    print_game_title()
    get_player_names()
    print("Hi", player1, "and", player2)
    display_game_board()
    
    while game_is_over == False:
        check_for_winner()
        if game_is_over == False:
            player_one_turn()
        else:
            game_over()
            break
        if game_is_over == False:
            player_two_turn()
        else:
            game_over()
            break
            
def restart_game():
    
    global game_is_over
    
    reset_board()
    print("\n" * 100)
    print("Hi", player1, "and", player2)
    display_game_board()
    
    while game_is_over == False:
        check_for_winner()
        if game_is_over == False:
            player_one_turn()
        else:
            game_over()
            break
        if game_is_over == False:
            player_two_turn()
        else:
            game_over()
            break
    
def print_game_title():
    
    print ("\n" * 100)
    print("  *** Welcome to Tic Tac Toe! ***")
    print ("\n" * 1)
    print("Use numbers 1-9 to select each square:")
    print("[1][2][3]")
    print("[4][5][6]")
    print("[7][8][9]")
   
    print ("\n" * 1)

#Game starts here

start_game()
