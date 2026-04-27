# David Orjuela
# Personal Project
import random as rand

board = None
captured = None
EMPTY = "____"

def initialize():
    board = [
        ["Rook", "Bishop", "Knight", "King", "Queen", "Knight", "Bishop", "Rook"],
        ["Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"],
        ["____", "____", "____", "____", "____", "____", "____", "____"],
        ["____", "____", "____", "____", "____", "____", "____", "____"],
        ["____", "____", "____", "____", "____", "____", "____", "____"],
        ["____", "____", "____", "____", "____", "____", "____", "____"],
        ["$Pawn", "$Pawn", "$Pawn", "$Pawn", "$Pawn", "$Pawn", "$Pawn", "$Pawn"],
        ["$Rook", "$Bishop", "$Knight", "$King", "$Queen", "$Knight", "$Bishop", "$Rook"],
    ]

    captured = [
        #[],
        #TODO: add another list linked to user
            ]
    print("... Chess board initialized.")
    print(f"Welcome, user! What gamemode would you like to play? Choose from below:")
    print(f"[1] - 2 Player Human Mode (Alternating)\n[2] - 1 Player vs Bot")

    # TODO: prompt user for username, store points across games

    return board, captured

def print_board():
    total = 8
    print(f"   {(" "*4)}1{(" "*8)}2{(" "*8)}3{(" "*8)}4{(" "*8)}5{(" "*8)}6{(" "*8)}7{(" "*8)}8",end="")
    print(f"\n  {"-"*(total*(8+1)+1)}")
    for i, piece in enumerate(board):
        print(f"{chr(i+65)} |",end="")
        for j,piece in enumerate(board[i]):
            word_size = len(piece)
            cell_size = total-word_size
            padding = cell_size//2
            # Pick a cell size that fits all words. Longest word is "$Bishop", which is 7 characters. \
            # Thus, with a 1 space padding on both sides, all cells will be 10 charaters wide. If odd, \
            # add 1 to the right side (or left, but in this case right).
            if(word_size % 2 == 0):
                print(f"{padding*" "}{piece}{padding*" "}|",end="")
            else:
                print(f"{(padding)*" "}{piece}{(padding+1)*" "}|",end="")

        print(f"\n  {"-"*(total*(8+1)+1)}",end="")
        print("")

def print_captured():
    if len(captured) is not None:
        print("Captured Pieces:")
        for piece in captured:
            print(f"{piece} | ",end="")
        print("")

def show_instructions():
    # TODO: Generate chess rules for user
    print("Welcome to Chess V1, created by David Orjuela!" \
    "\nThere are two sides: White and Black. White always plays first, though this player will be decided by chance." \
    "\nTo move a piece when prompted to play, type the coordinates of the piece you would like to move, " \
    "followed by the coordinates of the last square you are moving to." \
    "\nFor example, to move a Pawn located at B2 to C2 (one square down), type '> B2C2'. Happy Chessing!")    

def convert_coords(move_str: str):
    # all x's are letters and must be mapped to indexes (use ASCII)
    # all y's are +1 from index based 0
    return ord(move_str[0].upper())-65, int(move_str[1])-1, ord(move_str[2].upper())-65, int(move_str[3])-1
    
def in_bounds(x, y):
    return (x < 8 and x >= 0 and y < 8 and y >= 0)

# Function to count "jumps" between [start and end) moves -- another piece being in the path. Piece at end coords is a capture.
def jump(piece: str, x1,y1,x2,y2):
    jumps = 0
    if piece == "Rook":
        for x in range(x1+1,x2):
            if board[x][y1] != EMPTY:
                jumps += 1
        for y in range(y1+1, y2):
            if board[x1][y] != EMPTY:
                jumps += 1        
    return jumps

# Returns true only if the end coords coincide with a non-King piece. Assume coords are valid.
def piece_captured(end_x: int, end_y: int):
    # TODO: add checkmate logic
    if board[end_x][end_y] is not EMPTY and \
        board[end_x][end_y].strip("$") != "King":
        return True

def move_is_valid(piece: str, start_x, start_y, end_x, end_y):
    if not in_bounds(start_x, start_y) or not in_bounds(end_x, end_y): return False
    if piece.endswith("Rook"):
        # Check that Rook movements are only left/right or up/down and no jumps are made:
        if (start_x == end_x and start_y != end_y) or (start_y == end_y and start_x != end_x): #and jump("Rook", start_x, start_y, end_x, end_y) == 0:

            jump_count = jump("Rook", start_x, start_y, end_x, end_y) #TODO: combine with above when not debugging
            
            print(f"[DEBUG] Jump count: {jump_count}")
            if jump_count == 0:
                return True
        else:
            print("That was an invalid move for a Rook.")
    elif piece.endswith("Bishop"):
        pass
    elif piece.endswith("Knight"):
        pass
    elif piece.endswith("Queen"):
        pass
    elif piece.endswith("King"):
        pass
    elif piece.endswith("Pawn"):
        pass
    else:
        return False
        
def move(player, move_str):
    # Convert coordinates from user input (letters + numbers) to array indexes
    start_x, start_y, end_x, end_y = convert_coords(move_str)
    
    # User input split for printing purposes
    start_pos = f"{move_str[0]+move_str[1]}"
    end_pos = f"{move_str[2]+move_str[3]}"
    # Piece name extracted
    piece = board[start_x][start_y].strip("$")
    if board[end_x][end_y].startswith("$"):
        pass
    # If move is valid, check for any "kills" TODO: checkmates
    if move_is_valid(piece, start_x, start_y, end_x, end_y):
        piece_was_taken = piece_captured(end_x, end_y)
        print(f"[DEBUG] Piece Captured Bool: {piece_was_taken}")

        if piece_was_taken:
            captured.append(board[end_x][end_y])
    
            board[end_x][end_y] = board[start_x][start_y]
            board[start_x][start_y] = EMPTY

            print(f"{player} has moved their {piece} from {start_pos} to {end_pos}!")
    else:
        print("Move is not valid! Try again. ")
        return False
        # Prompt user to retry: invalid move TODO: give reason, return codes
        pass

    print_captured()
    print_board()

    return True


if __name__ == "__main__":
    board, captured = initialize()
    user_input = input("> ")
    if(user_input == "1"):
        # 2 Player Human Mode
        # Show instructions
        user_input = input("View instructions? n/Y").lower()
        if(user_input == "" or user_input == "n"):
            pass
        elif user_input == "y":
            show_instructions()
        print_board()
        players = ["White", "Black"]
        player_num = rand.randint(0,1)
        while(True): # Game Loop
            player = players[player_num]

            move_str = input(f"{player} to Move: >")
            #validate_move(move_str)
            if len(move_str) != 4:
                print("Invalid move! Please write the moving piece's coordinates followed by the end coordinates as such: {LETTER}{number}{LETTER}{number}")
            # If unable to move piece, repeat prompt to move.
            if not move(player, move_str):
                continue 

            player_num = (player_num + 1) % 2 # Next player
            

    else:
        print("Invalid game input.")
        # 1 Player vs Bot
        pass
