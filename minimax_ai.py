import engine as ttt
import copy


def minimax_ai(board, who_am_i):
    best_move = None
    best_score = None

    for move in _get_all_legal_moves(board):
        _board = copy.deepcopy(board)
        ttt.make_move(who_am_i, _board, move)

        opp = _get_opponent(who_am_i)
        score = _minimax_score(_board, opp, who_am_i)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move

def _minimax_score(board, player_to_move, player_to_optimize):
    winner = ttt.get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif ttt.is_board_full(board):
        return 0

    legal_moves = _get_all_legal_moves(board)

    scores = []
    for move in legal_moves:
        _board = copy.deepcopy(board)
        ttt.make_move(player_to_move, _board, move)

        opp = _get_opponent(player_to_move)
        opp_best_response_score = _minimax_score(_board, opp, player_to_optimize)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)


def _get_opponent(who_am_i):
    if who_am_i == 'X':
        return 'O'
    else:
        return 'X'


def _get_all_legal_moves(board):
    empty_coords = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val is None:
                empty_coords.append((x, y))
    return empty_coords

