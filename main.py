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

    #checking vertically
    if column == 0:
        for _ in range(3):
            
            if board[row][column] == board[row + 1][column] and board[row + 1][column] == board[row + 2][column]:
                print("Win")
            


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

    # Game loop
    for _ in range(5):
        # Player's move
        print("Your turn!")
        user_choice_row = int(input('Enter row (0, 1, 2): '))
        user_choice_column = int(input('Enter column (0, 1, 2): '))

        if _ == 0 :
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

        # Computer's move
        print("Computer's turn!")
        make_computer_move(board, computer_symbol)

        # Display the board after the computer's move
        display_board(board)

        if _ >= 2:
            game_brain(board,starting_pos)
            break
        # Check if the computer has won (you can implement this later)
        # if check_win(board, computer_symbol):
        #     print("Computer wins!")
        #     break

# Start the game
play_game()
