import random

BOARD_WIDTH = 3
BOARD_HEIGHT = 3


def human_player(board, who_am_i):
    x_co_ord = int(raw_input("X?: "))
    y_co_ord = int(raw_input("Y?: "))
    return (x_co_ord, y_co_ord)


def random_ai(board, who_am_i):
    return _random_move(board)


def finds_own_winning_moves_ai(board, who_am_i):
    my_winning_move = _find_winning_move(board, who_am_i)
    if my_winning_move:
        return my_winning_move
    else:
        return _random_move(board)

def blocks_their_winning_moves_ai(board, who_am_i):
    their_winning_move = _find_winning_move(board, utils.get_opponent(who_am_i))
    if their_winning_move:
        return their_winning_move
    else:
        return _random_move(board)


def finds_all_winning_moves_ai(board, who_am_i):
    my_winning_move = _find_winning_move(board, who_am_i)
    if my_winning_move:
        return my_winning_move

    their_winning_move = _find_winning_move(board, utils.get_opponent(who_am_i))
    if their_winning_move:
        return their_winning_move

    return _random_move(board)


def _find_winning_move(board, who_am_i):
    all_line_co_ords = _get_all_line_co_ords()

    for line in all_line_co_ords:
        n_me = 0
        n_them = 0
        n_new = 0
        last_new_co_ord = None

        for (x, y) in line:
            value = board[x][y]
            if value == who_am_i:
                n_me += 1
            elif value is None:
                n_new += 1
                last_new_co_ord = (x, y)
            else:
                n_them += 1

        if n_me == 2 and n_new == 1:
            return last_new_co_ord


def _random_move(board):
    legal_moves = utils.get_all_legal_moves(board)
    return random.choice(legal_moves)


def _get_all_line_co_ords():
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
