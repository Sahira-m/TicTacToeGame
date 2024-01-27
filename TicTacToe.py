# from IPython.display import clear_output
import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board, position
    ):
        position = int(input("choose a position 1 to 9     "))
    return position


def replay():
    choice = input("Play Again? Y or N")
    return choice == "Y"


def display_board(board):
    # clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-------")
    print(board[1] + "|" + board[2] + "|" + board[3])


test_Board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
# display_board(test_Board)


#def player_input():
 #   marker = ""
 #   while marker != "X" and marker != "O":
  #      marker = input("player1 choose X or  O      ")
   # if marker == "X":
    #    return ("X", "O")
    #else:
     #   return ("O", "X")


player1="X"
player2 ="Y"
print("player1 sympol is", player1, "player2 sympol is ", player2)


def place_marker(board, marker, position):
    print("Marker ", marker, "pos", position)
    board[position] = marker


# place_marker(test_Board, "X", 5)
# display_board(test_Board)


def win_check(board, mark):
    # rows or coloums or diagonally same marker then win based on player marker sympol
    return (
        (board[1] == board[2] == board[3] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[7] == board[8] == board[9] == mark)
        or (board[7] == board[4] == board[1] == mark)
        or (board[8] == board[5] == board[2] == mark)
        or (board[9] == board[6] == board[3] == mark)
        or (board[7] == board[5] == board[3] == mark)
        or (board[1] == board[5] == board[9] == mark)
    )


# print(win_check(test_Board, "X"))
#Start Game
print("WELCOME TO TIC TAC TOE GAME")
while True:
    # play the game
    # set everything up board,whose first,choose markers
    the_board = [" "] * 10
    #player1, player2 = player_input()
    print("player1 sympol is", player1, "player2 sympol is ", player2)
    turn = choose_first()
    print(turn + "  Will go first")
    play_game = input("Ready to play? Y or  N       :")
    if play_game == "Y":
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "Player 1":
            # show board

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1, position)

            if win_check(the_board, player1):
                display_board(the_board)
                print("Congratulations! You have won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2, position)

            if win_check(the_board, player2):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
