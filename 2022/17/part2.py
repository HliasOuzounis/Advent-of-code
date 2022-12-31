from copy import deepcopy

class Rock:
    def __init__(self, stop_conditions, left_conditions, right_conditions, height, length, shape):
        self.stop_conditions = stop_conditions
        self.left_conditions = left_conditions
        self.right_conditions = right_conditions
        self.height = height
        self.length = length
        self.shape = shape
        self.pos = (3, 3)

def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def main():
    wind = [-1 if char == "<" else 1 for char in open("input.txt").read().strip()]
    wind_index = 0
    wind_mod = len(wind)

    rocks = [
        (((1, 0), (1, 1), (1, 2), (1, 3)), [(0, -1)], [(0, 4)], 1, 4, ((0, 0), (0, 1), (0, 2), (0, 3))),
        (((0, 0), (1, 1), (0, 2)), ((0, 0), (-1, -1), (-2, 0)), ((0, 2), (-1, 3), (-2, 2)), 3, 3, ((-1, 0), (0, 1), (-1, 1), (-1, 2), (-2, 1))),
        (((1, 0), (1, 1), (1, 2)), [(0, -1)], ((0, 3), (-1, 3), (-2, 3)), 3, 3, ((0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2))),
        ([(1, 0)], ((0, -1), (-1, -1), (-2, -1), (-3, -1)), ((0, 1), (-1, 1), (-2, 1), (-3, 1)), 4, 1, ((0, 0), (-1, 0), (-2, 0), (-3, 0))),
        (((1, 0), (1, 1)), ((0, -1), (-1, -1)), ((0, 2), (-1, 2)), 2, 2, ((0, 0), (0, 1), (-1, 0), (-1, 1))),
    ]

    board = [[1] + [0] * 7 + [1] for i in range(7)] + [[1] * (4 + 2 + 1 + 2)]
    # iterations = 2022 + 1
    iterations = 5 * wind_mod * 3
    height = find_height(wind, wind_index, wind_mod, rocks, deepcopy(board), iterations)
    
    
    target = 10**12
    # target = 1_000_000_000_000
    n = target//iterations
    remaining = target % iterations

    # mod_board = []
    # for line in open("notes.txt"):
    #     row = []
    #     for char in line:
    #         row.append(char == "#")
    #     mod_board.append(row)   
        
    print(height * n + find_height(wind, wind_index, wind_mod, rocks, deepcopy(board), remaining + 1))


def find_height(wind, wind_index, wind_mod, rocks, board, iterations):
    height = 0
    max_pos = 7
    for n in range(iterations):
    # for i in range(7):
        rock = Rock(*rocks[n % 5])
        while True:
            wind_dir = wind[wind_index]
            if wind_dir == 1:
                if not any(
                    board[i][j] for i, j in (add(rock.pos, stop_cond) for stop_cond in rock.right_conditions) 
                ):
                    rock.pos = (rock.pos[0], rock.pos[1] + 1)
            if wind_dir == -1:
                if not any(
                    board[i][j] for i, j in (add(rock.pos, stop_cond) for stop_cond in rock.left_conditions) 
                ):  
                    rock.pos = (rock.pos[0], rock.pos[1] - 1)

            wind_index = (wind_index + 1) % wind_mod

            if any(
                board[i][j] for i, j in (add(rock.pos, stop_cond) for stop_cond in rock.stop_conditions) 
            ):  
                for i, j in (add(rock.pos, shape) for shape in rock.shape):
                    board[i][j] = 1
                # print_board(board)

                new_max = min(max_pos, rock.pos[0] - rock.height + 1)
                height_added = max_pos - new_max
                height += height_added
                board = [[1] + [0] * 7 + [1] for _i in range(height_added)] + board

                # print(wind_index, wind_dir)
                try:
                    new_floor = board.find([1] * 9)
                    board = board[:new_floor + 1]
                except:
                    pass
                break

            rock.pos = (rock.pos[0] + 1, rock.pos[1])

    return height - height_added

# def print_board(board):
#     for line in board:
#         for j in line:
#             print("#" if j else ".", end="")
#         print()
#     print("Next board")

if __name__ == "__main__":
    main()
