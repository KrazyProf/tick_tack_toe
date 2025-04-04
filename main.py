import random

# Graffiti (Welcome Message)
def display_graffiti():
    print("***************************************")
    print("*                                     *")
    print("*  Welcome to Tic-Tac-Toe!            *")
    print("*  Get ready to challenge the computer*")
    print("*                                     *")
    print("***************************************")
    print()

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

# Step 4: Check for a Win or Draw
def game_brain(board, symbol):
    # Check rows for a win
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True

    # No win found
    return False

# Step 5: Check if the board is full (draw)
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Step 6: Main Game Logic
def play_game():
    display_graffiti()  # Display the welcome message

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

    # Game loop
    while True:
        # Player's move
        print("Your turn!")
        user_choice_row = int(input('Enter row (0, 1, 2): '))
        user_choice_column = int(input('Enter column (0, 1, 2): '))

        # Check if the cell is empty
        if board[user_choice_row][user_choice_column] == ' ':
            board[user_choice_row][user_choice_column] = user_symbol
        else:
            print("That cell is already occupied! Try again.")
            continue

        # Display the board after the player's move
        display_board(board)

        # Check if the player has won
        if game_brain(board, user_symbol):
            print("Congratulations! You win!")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn!")
        make_computer_move(board, computer_symbol)

        # Display the board after the computer's move
        display_board(board)

        # Check if the computer has won
        if game_brain(board, computer_symbol):
            print("Computer wins! Better luck next time.")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print("It's a draw!")
            break


# Start the game
play_game()