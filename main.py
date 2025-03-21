# #TODO:
# 1. Define the Game Board -> Represent the game board as a 3x3 grid. You can use a list of lists 
# (e.g., board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
# 2. Display the Board -> Create a function to display the current state of the board
# 3. Handle Player Input -> Ask the current player (either X or O) to input their move. 
# You can prompt them to enter the row and column numbers (e.g., 1, 1 for the top-left corner).
# 4. Check for a Win or Draw
# 5. Repeat Until Game Ends

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

# Example usage     
# board[2][0] = "X"
# board[1][2] = 'O'
display_board(board)


user_input = input('Do you want to as "X" or "O": ')
computer = ''
if user_input == 'X':
    computer = 'O'
else:
    computer = 'X'


