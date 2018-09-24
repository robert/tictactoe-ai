import sys

import engine as ttt
import heuristic_ais as ai
import minimax_ai as mm

if __name__ == "__main__":
    p1_name = sys.argv[1]
    p2_name = sys.argv[2]

    ttt.play(p1_name, p2_name)
