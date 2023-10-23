def print_board(board):
    for row in board[::-1]:
        print(" ".join(row))
    print()
    # print out board in reverse


def initialize_board(num_rows, num_cols):
    board = [['-' for _ in range(num_cols)] for _ in range(num_rows)]
    return board
    # print full board based on user input


def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row
    return -1
    # based on user input put the chip where input


# determines if either play has a connect 4
def check_if_winner(board, col, row, chip_type):
    def check_horizontal():
        count = 0
        for x in range(len(board[0])):
            if board[row][x] == chip_type:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        return False

    def check_vertical():
        count = 0
        for y in range(len(board)):
            if board[y][col] == chip_type:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        return False

    return check_horizontal() or check_vertical()


if __name__ == "__main__":
    # determine size of board
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))

    # if board is not 4x4 let user know
    if num_rows < 4 or num_cols < 4:
        print("The board dimensions should be 4x4 or greater.")
    else:
        # print out board
        board = initialize_board(num_rows, num_cols)
        print_board(board)
        print("Player 1: x")
        print("Player 2: o")
        print()

        players = ['x', 'o']
        player_names = ['Player 1', 'Player 2']
        current_player = 0
        moves = 0

        # ensure that the board allows input if not full
        while moves < num_rows * num_cols:
            col = int(input(f"{player_names[current_player]}: Which column would you like to choose? "))
            if 0 <= col < num_cols:
                row = insert_chip(board, col, players[current_player])
                if row != -1:
                    print_board(board)
                    if check_if_winner(board, col, row, players[current_player]):
                        print(f"{player_names[current_player]} won the game!")
                        break
                    current_player = 1 - current_player
                    moves += 1
                else:
                    print("The selected column is already full. Try again.")
            else:
                print("Invalid column number. Please choose a valid column.")

        if moves == num_rows * num_cols:
            print("Draw. Nobody wins.")
