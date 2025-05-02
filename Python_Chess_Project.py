import string #module to use for ascii (alphabet letters)

# Checks if position is valid on a chessboard, letter (a-h) and a digit (1-8)
def is_valid_position(pos): #pos for position
    if len(pos) != 2: #lenght of input 2 characters
        return False
    column, row = pos[0], pos[1] #asigning to column(1st character) and row(2nd)
    return (
    column in string.ascii_lowercase[:8] and # Check if column is btw a-h, [:8] first letters
    row in "12345678" # Check if row is btw 1-8
)

# Draw  board. 8x8 chessboard grid.
def initialize_board():
    return [['__' for i in range(8)] #creates list of lists, where each inner list represents a row on the board
            for i in range(8)]


#Prints the visual chessboard, col a-h, rows 1-8
def print_board(board):
    print("  a  b  c  d  e  f  g  h")  # Column labels
    for row in range(8, 0, -1): #loop iterates over rows in reverse order, range(start, stop, step)
        row_display = [f"{row}"]  # Row label
        for col in range(8): # loop iterates over the columns (0 to 7)
            row_display.append(board[row-1][col]) #append columns (loop iterates from 8 to 1, -1 aligns row number with list index.)
        for item in row_display:
            print(item, end=" ")
        print()  
    print()


# Converts a board position (e.g., 'a1') to row and column indices for the board list.
# e.g. a - column 0;
# e.g. 1 - row 0.
def position_to_indices(pos):
    col = ord(pos[0]) - ord('a')  # Convert column letter to index (0-7)
    row = int(pos[1]) - 1         # Convert row number to index (0-7)
    return row, col


# Users input for white piece and its position.
def get_white_piece(board):

    piece_symbols = {'knight': 'WN', 'rook': 'WR'}  # Symbols for white pieces
    while True:
        user_input = input("Enter the white piece and its position (knight or rook from a1-h8): ").lower().split()
        if (
            len(user_input) == 2 #user input contains 2 elements
            and user_input[0] in piece_symbols #check if first element is part of sybols dict
            and is_valid_position(user_input[1]) #check if its in board possition
        ):
            row, col = position_to_indices(user_input[1]) #converting to board
            board[row][col] = piece_symbols[user_input[0]]  # Place the white piece on the board
            print(f"\nWhite {user_input[0]} placed at {user_input[1]}.\n") #\n to add blank lines in output
            print_board(board)
            return user_input[0], user_input[1]  # Return piece type and position
        else:
            print("Invalid input. Please enter a valid piece and position.")


# Input black pieces and their positions.
def get_black_pieces(board):
    black_pieces = {}  # Dictionary to store black pieces and positions
    piece_symbols = {'king': 'BK', 'queen': 'BQ', 'rook': 'BR', 'bishop': 'BB', 'knight': 'BN', 'pawn': 'BP'}
    print("Enter black pieces (e.g., pawn d4). Type 'done' when finished:")
    while len(black_pieces) < 16:
        user_input = input().lower().split()
        if user_input[0] == "done":
            if black_pieces:
                break  # Exit loop if at least one black piece has been added
            else:
                print("You must add at least one black piece before typing 'done'.")
                continue
        if len(user_input) == 2 and user_input[0] in piece_symbols and is_valid_position(user_input[1]): #same check as for whites
            row, col = position_to_indices(user_input[1])
            if board[row][col] == '__': #additional check for occupied places
                board[row][col] = piece_symbols[user_input[0]]  # Place the black piece on the board
                black_pieces[user_input[1]] = user_input[0]     # Add to the dictionary
                print(f"\nBlack {user_input[0]} placed at {user_input[1]}.\n")
                print_board(board)
            else:
                print("Position is already occupied. Choose a different position.")
        else:
            print("Invalid input. Try again.")
    return black_pieces


# Returns a list of all possible moves for a knight from the given position.
def get_knight_moves(pos):
    col, row = pos[0], int(pos[1]) #column - first character of position, row converted to int of second character of pos
    # Possible moves for knight (change in direction (d): dx - column, dy - row)
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    valid_moves = [] # empty list to store valid move positions
    for dx, dy in moves: # go through possible moves
        new_col = chr(ord(col) + dx) # Calculate the new column and row. (ord() gives numerical value (ASCII), chr reverts back
        new_row = row + dy # Form the new position
        new_pos = f"{new_col}{new_row}"
        if is_valid_position(new_pos): # Check if the new position is valid
            valid_moves.append(new_pos) # Add the valid position to the list
    return valid_moves # Return the list of valid moves

##Notes
# ord () and chr() functions of Python are built-in functions 
# that are used to convert a character to an integer and vice-versa.

# Returns a list of all possible moves for a rook from the given position.
def get_rook_moves(pos, black_pieces):
    col, row = ord(pos[0]) - ord('a'), int(pos[1]) 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Directions a rook can move: right, left, up, down
    valid_moves = []
    for dx, dy in directions:
        x, y = col, row
        while True:
            x, y = x + dx, y + dy  # Update x and y (adding dx and dy)
            if not (0 <= x < 8 and 1 <= y <= 8): # Stop if the new position is off the board
                break  
            new_pos = f"{chr(ord('a') + x)}{y}"  ### letter position (ord() gives numerical value, chr reverts back
            valid_moves.append(new_pos)
            if new_pos in black_pieces:
                break  # Stop if a black piece is encountered
    return valid_moves


# What black figures can be captured by the white rook/knight from its position.
def find_capture(white_piece, position, black_pieces):

    if white_piece == "knight":
        possible_moves = get_knight_moves(position)
    else:
        possible_moves = get_rook_moves(position, black_pieces)
    
    # Return a dictionary of capturable black pieces
    capturable_pieces = {}
    for pos, piece in black_pieces.items(): #.items displays a list of the dictionary's key-value pairs as tuples
        if pos in possible_moves: #checks if current pos is in list of moves white can make
            capturable_pieces[pos] = piece #adds position and black piece to dict

    return capturable_pieces
    
def main():
    board = initialize_board()
    white_piece, white_position = get_white_piece(board)
    black_pieces = get_black_pieces(board)
    capturable = find_capture(white_piece, white_position, black_pieces)
    
    if capturable:
        print("The white piece can capture these black pieces:")
        for pos, piece in capturable.items(): # Loop through each position and piece in capturable dict
            print(f"{piece} at {pos}")
    else:
        print("No black pieces can be captured.")

if __name__ == "__main__": #spec. string in Python that indicates a module is being run as the main program.


    main()


#Notes for future can use chess library? import chess def get_rook_moves(board, position)
   
