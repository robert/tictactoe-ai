

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
    columns = board
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)

    diagonals = [
        [
            board[0][0],
            board[1][1],
            board[2][2]
        ],
        [
            board[0][2],
            board[1][1],
            board[2][0]
        ]
    ]
    all_possible_lines = columns + rows + diagonals

    for line in all_possible_lines:
        if len(set(line)) == 1 and line[0] is not None:
            return line[0]

    return None


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

        move_co_ords = human_player(board, player_symbol)
        make_move(player_symbol, board, move_co_ords)

        winner = get_winner(board)
        if winner is not None:
            render(board)
            print "THE WINNER IS %s!" % winner
            break
        turn_number += 1


def human_player(board, who_am_i):
    x_co_ord = int(raw_input("X"))
    y_co_ord = int(raw_input("Y"))
    return (x_co_ord, y_co_ord)

play(human_player, human_player)
