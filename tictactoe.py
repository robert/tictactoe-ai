import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3

def blank_board():
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


def play(player_x_function, player_o_function):
    players = [
        (player_x_function, 'X'),
        (player_o_function, 'O'),
    ]

    turn_number = 0
    board = blank_board()
    while True:
        player_function, player_symbol = players[turn_number % 2]
        render(board)

        move_co_ords = player_function(board, player_symbol)
        make_move(player_symbol, board, move_co_ords)

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


def human_player(board, who_am_i):
    x_co_ord = int(raw_input("X"))
    y_co_ord = int(raw_input("Y"))
    return (x_co_ord, y_co_ord)

def random_ai(board, who_am_i):
    return random_move(board)


def random_move(board):
    empty_co_ords = []
    for x in range(0, BOARD_WIDTH):
        for y in range(0, BOARD_HEIGHT):
            if board[x][y] is None:
                empty_co_ords.append((x, y))
    return random.choice(empty_co_ords)

def opponent(who_am_i):
    if who_am_i == 'X':
        return 'O'
    else:
        return 'X'

def finds_own_winning_moves_ai(board, who_am_i):
    my_winning_move = find_winning_move(board, who_am_i)
    if my_winning_move:
        return my_winning_move

    return random_move(board)

def blocks_their_winning_moves_ai(board, who_am_i):
    their_winning_move = find_winning_move(board, opponent(who_am_i))
    if their_winning_move:
        return their_winning_move

    return random_move(board)

def finds_all_winning_moves_ai(board, who_am_i):
    my_winning_move = find_winning_move(board, who_am_i)
    if my_winning_move:
        return my_winning_move

    their_winning_move = find_winning_move(board, opponent(who_am_i))
    if their_winning_move:
        return their_winning_move

    return random_move(board)

def find_winning_move(board, who_am_i):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        n_me = 0
        n_them = 0
        n_blank = 0
        last_blank_co_ord = None

        for (x, y) in line:
            value = board[x][y]
            if value == who_am_i:
                n_me += 1
            elif value is None:
                n_blank += 1
                last_blank_co_ord = (x, y)
            else:
                n_them += 1

        if n_me == 2 and n_blank == 1:
            return last_blank_co_ord

play(finds_all_winning_moves_ai, blocks_their_winning_moves_ai)
