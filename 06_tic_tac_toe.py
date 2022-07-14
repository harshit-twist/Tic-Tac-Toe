import random
import time

turn = None
board = ['1','2','3','4','5','6','7','8','9']


def game_board():
    # Visualize the Tic Tac Toe game board
    print()
    print(" {} | {} | {}  ".format(board[0],board[1],board[2]))
    print("___|___|___")
    print(" {} | {} | {}  ".format(board[3],board[4],board[5]))
    print("___|___|___")
    print(" {} | {} | {}   ".format(board[6],board[7],board[8]))
    print("   |   |   ")
    print()


def check_conds(player_1,player_2,choice1,choice2,total_moves_done):
    # checking conditions who is winning

    if (board[0]==board[1]==board[2]==choice1) or (board[3]==board[4]==board[5]==choice1) or (board[6]==board[7]==board[8]==choice1) or (board[0]==board[3]==board[6]==choice1) or (board[1]==board[4]==board[7]==choice1) or (board[2]==board[5]==board[8]==choice1) or (board[0]==board[4]==board[8]==choice1) or (board[2]==board[4]==board[6]==choice1):
        print(f"\n{player_1} wins\n")
        return True

    elif (board[0]==board[1]==board[2]==choice2) or (board[3]==board[4]==board[5]==choice2) or (board[6]==board[7]==board[8]==choice2) or (board[0]==board[3]==board[6]==choice2) or (board[1]==board[4]==board[7]==choice2) or (board[2]==board[5]==board[8]==choice2) or (board[0]==board[4]==board[8]==choice2) or (board[2]==board[4]==board[6]==choice2):
        print(f"\n{player_2} wins\n")
        return True

    elif total_moves_done == 9:
        print("\nDraw\n")
        return True
    
    return False


def player_player():
    # Two real players playing game

    global board, turn

    game_board()

    print("\nWelcome Player 'A' and Player 'B'")

    choices = ['X','O'] 

    player_a_mark = random.choice(choices)     # radomly chooses a mark for first player
    choices.remove(player_a_mark)
    player_b_mark = choices.pop()              # other mark is given to second player

    print("-->A player's mark: {}\n-->B player's mark: {}".format(player_a_mark , player_b_mark))

    turn = random.choice([0,1])                 # giving first turn radomly to any player

    total_moves_done = 1
    filled_move = []

    if turn == 0:
        print("\n*** Player A has 1st move ***\n")
    else:
        print("\n*** Player B has 1st move ***\n")
    
    while total_moves_done <= 9:

        if turn == 0:
            player_a_move = int(input("Player A make your move ({}): ".format(player_a_mark)))

            if player_a_move not in range(1,10) or player_a_move in filled_move:
                # prevents player A to use invalid move or used move

                print("\nInvalid move. Choose again")
                continue

            board[player_a_move - 1] = player_a_mark    # put player A's mark on selected location
            filled_move.append(player_a_move)

        elif turn == 1:
            player_b_move = int(input("Player B make your move ({}): ".format(player_b_mark)))
           
            if player_b_move not in range(1,10) or player_b_move in filled_move:
                # prevents player B to use invalid move or used move

                print("\nInvalid move. Choose again")
                continue

            board[player_b_move-1] = player_b_mark      # put player B's mark on selected location
            filled_move.append(player_b_move)
        
        game_board()        # shows current status of game board on screen

        if total_moves_done >=5:
            # To end the game, minimum 5 moves required, no need to check conditions before that
            
            if check_conds('Player A', 'Player B' , player_a_mark , player_b_mark,total_moves_done):
                return
      
        turn = 1 - turn         # changes player's turn
        total_moves_done += 1


def player_computer():
    # A real player playing with computer
    
    global board, turn
    
    game_board()

    print("\nWelcome Player A and Mr Computer")

    choices = ['X','O']

    player_a_mark = random.choice(choices)          # radomly chooses a mark for first player
    choices.remove(player_a_mark)
    comp_mark = choices.pop()                       # other mark is given to computer

    print("-->A player's mark: {}\n-->Mr Computer's mark: {}".format(player_a_mark , comp_mark))

    turn = random.choice([0,1])                     # giving first turn radomly to any player

    total_moves_done = 1
    valid_moves = [1,2,3,4,5,6,7,8,9]
    filled_move = []

    if turn == 0:
        print("\n*** Player A has 1st move ***\n")
    else:
        print("\n*** Mr Computer has 1st move ***\n")
    
    while total_moves_done <= 9:

        if turn == 0:
            player_a_move = int(input("Player A make your move ({}): ".format(player_a_mark)))

            if player_a_move not in range(1,10) or player_a_move in filled_move:
                # prevents player A to use invalid move or used move

                print("\nInvalid move. Choose again")
                continue

            board[player_a_move-1] = player_a_mark          # put player A's mark on selected location
            filled_move.append(player_a_move)
            valid_moves.remove(player_a_move)

        elif turn == 1:
            print("Mr Computer thinking of its move... ")
            time.sleep(5)

            comp_move = random.choice(valid_moves)           # computer can't make invalid move

            print("Mr Computer's move ({}) : {}".format(comp_mark,comp_move))

            board[comp_move-1] = comp_mark                  # put computer's mark on selected location
            filled_move.append(comp_move)
            valid_moves.remove(comp_move)
        
        game_board()

        if total_moves_done >=5:
            # To end the game, minimum 5 moves required, no need to check conditions before that

            if check_conds('Player A', 'Mr Computer' , player_a_mark , comp_mark , total_moves_done):
                return
      
        turn = 1 - turn     # changes player's turn
        total_moves_done += 1


def computer_computer():
    # Computer playing with itself

    global board, turn
    
    game_board()
    print("\nWelcome Mr Jarvis and Mr Ultron")      # radomly chooses a mark for Jarvis
    choices = ['X','O']

    jarvis_mark = random.choice(choices)
    choices.remove(jarvis_mark)
    ultron_mark = choices.pop()                     # other mark is given to Ultron

    print("--> Jarvis's mark: {}\n--> Ultron's mark: {}".format(jarvis_mark , ultron_mark))

    turn = random.choice([0,1])

    total_moves_done = 1
    valid_moves = [1,2,3,4,5,6,7,8,9]
    filled_move = []

    if turn == 0:
        print("\n*** Jarvis has 1st move ***\n")
    else:
        print("\n*** Ultron has 1st move ***\n")
    
    while total_moves_done <= 9:

        if turn == 0:
            print("Jarvis thinking of its move... ")
            time.sleep(5)

            jarvis_move = random.choice(valid_moves)
            print("Jarvis's move ({}) : {}".format(jarvis_mark,jarvis_move))


            board[jarvis_move-1] = jarvis_mark  

            filled_move.append(jarvis_move)
            valid_moves.remove(jarvis_move)

        elif turn == 1:
            print("Ultron thinking of its move... ")
            time.sleep(5)

            ultron_move = random.choice(valid_moves)
            print("Ultron's move ({}) : {}".format(ultron_mark,ultron_move))

            board[ultron_move-1] = ultron_mark

            filled_move.append(ultron_move)
            valid_moves.remove(ultron_move)
        
        game_board()

        if total_moves_done >=5:
            # To end the game, minimum 5 moves required, no need to check conditions before that

            if check_conds('Jarvis', 'Ultron' , jarvis_mark , ultron_mark , total_moves_done):
                return
      
        turn = 1 - turn     # changes player's turn
        total_moves_done += 1


def play():

    print("\nWelcome to Tic Tac Toe. There are 3 types of games present.")
    print("1. Player with other player\n2. Player with computer\n3. Computer with computer\n")
    game_code = int(input("Enter your game code (1 or 2 or 3): "))

    if game_code == 1:
        player_player()

    elif game_code == 2:
        player_computer()

    elif game_code == 3:
        computer_computer()

    else:
        print("Invalid game code. Choose again.")


while True:
    play()
    more_play = input("\nType 'more' to play again and 'end' to end the game: ")
    if more_play == 'more':
        continue
    elif more_play == 'end':
        print("\nThanks for playing. Come again.\n")
        break
