# making a dict of possible positions with fromkeys method and giving them value " "
board = dict.fromkeys(range(1, 10), ' ')
# print(board)
# {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def display_board():

    print(board[1], '|', board[2], '|', board[3])
    print("- - - - -")
    print(board[4], '|', board[5], '|', board[6])
    print("- - - - -")
    print(board[7], '|', board[8], '|', board[9])


def place_token(player_token, postion):
    """
    take a player token and place it in the given position
    """
    board[postion] = player_token


def token_choice():
    """
    ask what token player 1 wants to take and assign
    other token is assigned to player 2
    """
    token = ''
    while token not in ["X", "O"]:
        token = input('Player 1.. what token you want to choose?? ').upper()
        if token not in ["X", "O"]:
            print("Please enter X or O dammit ")
    if token == "X":
        player1_token = "X"
        player2_token = "O"
    else:
        player1_token = "O"
        player2_token = "X"
    return player1_token, player2_token


def position_choice():
    """
    Initializing variable position with None
    keep asking for position choice until the user inputs integer b/w 1 and 9

    Returns:
        [int]: [where player wants his token to be placed]
    """
    position_choice = ''

    while position_choice not in range(1, 10):
        position_choice = input('Enter position choice between 1 and 9 ')
        if position_choice.isdigit() == False:
            print('Enter a number dammit')
            continue
        else:
            position_choice = int(position_choice)

        if position_choice not in range(1, 10):
            print("Enter position choice between 1 and 9 dammit!!! ")


    return position_choice


def game_on():

    flag = None
    while flag not in ["Y", "N"]:
        flag = input('Shall we play ?').upper()
        if flag not in ["Y", "N"]:
            print('Enter Y or N dammit!!! ')
    if flag == 'Y':
        return True
    else:
        return False


def win_check(token):
    if  board[1] == board[2] == board[3] == token or \
        board[4] == board[5] == board[6] == token or \
        board[7] == board[8] == board[9] == token or \
        board[1] == board[4] == board[7] == token or \
        board[2] == board[5] == board[8] == token or \
        board[3] == board[6] == board[9] == token or \
        board[1] == board[5] == board[9] == token or \
        board[3] == board[5] == board[7] == token:
        return token


def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

game_on_choice = True
while True:
    print("Welcome to Tic Tac Toe")
    player1_token, player2_token = token_choice()

    while game_on_choice:

        print("Player1.. enter your position choice ")

        place_token(player1_token, position_choice())

        print("Player2.. enter your position choice ")

        place_token(player2_token, position_choice())

        if win_check(player1_token) == player1_token:
            print("Player 1 has won")
            break
        elif win_check(player2_token) == player2_token:
            print('Player 2 has won')
            break
        display_board()
        game_on_choice = game_on()
    if not replay():
        break
