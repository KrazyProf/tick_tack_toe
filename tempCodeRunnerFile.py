import random

# Step 1: Define the Game Board
# Initialize a 3x3 grid with empty spaces
board = [
    [' ', ' ', ' '],  # Row 1
    [' ', ' ', ' '],  # Row 2
    [' ', ' ', ' ']   # Row 3
]

# Step 2: Display the Board
def display_board(board):
    for i, row in enumerate(board):  # Loop through each row
        # Print the cells separated by '|'
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        
        # Print a horizontal line after the first and second rows
        if i < 2:
            print("-----------")

# Step 3: Computer's Move
def make_computer_move(board, computer_symbol):
    while True:
        # Randomly choose a row and column
        computer_choice_row = random.randint(0, 2)
        computer_choice_column = random.randint(0, 2)

        # Check if the cell is empty
        if board[computer_choice_row][computer_choice_column] == ' ':
            # Place the computer's symbol
            board[computer_choice_row][computer_choice_column] = computer_symbol
            break

def game_brain(board, position):
    
    row = position[0]
    column = position[1]

    reverse = 1
    sub_row = 1
    sub_column = 1

    if row == 2:
        reverse = -1
        sub_row = -1

    if column == 2:
        sub_column = -1
        reverse = -1
    #checking vertically
        
    if board[row][column] == board[row + reverse][column] and board[row + reverse][column] == board[row + (2 * reverse)][column]:
        print("Win")
        return True
    
    # checking horizontally
    
    if board[row][column] == board[row][column + reverse] and board[row][column + reverse] == board[row][column + (2 * reverse)]:
        print("Win")
        return True
     
    # checking diagonally
    if board[row][column] == board[row + sub_row][column + sub_column] and board[row + sub_row][column + sub_column] == board[row + (2 * sub_row)][column + (2 * sub_column)]:
        print('Win')
        return True
    



# Step 4: Main Game Logic
def play_game():
    # Ask the player to choose 'X' or 'O'
    user_input = input('Do you want to be "X" or "O": ').upper()
    while user_input not in ['X', 'O']:
        print('Invalid choice! Please choose "X" or "O".')
        user_input = input('Do you want to be "X" or "O": ').upper()

    # Assign symbols
    user_symbol = user_input
    
    computer_symbol = 'O' if user_symbol == 'X' else 'X'

    # Display the initial board
    display_board(board)

    is_over = False
    # Game loop
    i = 0
    while not is_over:

        # Checking if game is a draw
        # if ' ' not in board:
        #     is_over = True
        #     print("Draw")
        #     break
        # Player's move
        print("Your turn!")
        user_choice_row = int(input('Enter row (0, 1, 2): '))
        user_choice_column = int(input('Enter column (0, 1, 2): '))

        if i == 0 :
            starting_pos = [user_choice_row , user_choice_column]
        # Check if the cell is empty
        if board[user_choice_row][user_choice_column] == ' ':
            board[user_choice_row][user_choice_column] = user_symbol
        else:
            print("That cell is already occupied! Try again.")
            continue

        # Display the board after the player's move
        display_board(board)

        # Check if the player has won (you can implement this later)
        # if check_win(board, user_symbol):
        #     print("You win!")
        #     break

        if i >= 2:
            is_over = game_brain(board,starting_pos)
        # Check if the computer has won (you can implement this later)
        # if check_win(board, computer_symbol):
        #     print("Computer wins!")
        #     break
        # Computer's move
        print("Computer's turn!")
        make_computer_move(board, computer_symbol)

        # Display the board after the computer's move
        display_board(board)
        print(i)
        i += 1

# Start the game
play_game()
