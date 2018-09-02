import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def new_board():
    board = []
    for x in range(0, BOARD_WIDTH):
        column = []
        for y in range(0, BOARD_HEIGHT):
            column.append(None)
        board.append(column)

    return board


def get_winner(board):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None


def get_all_line_co_ords():
    cols = []
    for x in range(0, BOARD_WIDTH):
        col = []
        for y in range(0, BOARD_HEIGHT):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append((x, y))
        rows.append(row)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return cols + rows + diagonals

def render(board):
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    print '  0 1 2 '
    print '  ------'
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print "%d|%s|" % (row_num, ' '.join(output_row))
        row_num += 1
    print '  ------'


def make_move(player, board, move_co_ords):
    if board[move_co_ords[0]][move_co_ords[1]] is not None:
        raise Exception("Illegal move!")

    board[move_co_ords[0]][move_co_ords[1]] = player


def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is None:
                return False
    return True


def play():
    players = ['X', 'O']

    turn_number = 0
    board = new_board()
    while True:
        current_player = players[turn_number % 2]
        render(board)

        move_co_ords = get_move()
        make_move(current_player, board, move_co_ords)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print "THE WINNER IS %s!" % winner
            break

        if is_board_full(board):
            render(board)
            print "IT'S A DRAW!"
            break

        turn_number += 1

def get_move():
    x_co_ord = int(raw_input("What is your X co-ordinate?: "))
    y_co_ord = int(raw_input("What is your Y co-ordinate?: "))
    print ""
    return (x_co_ord, y_co_ord)

play()
