import time
from functools import lru_cache
room_size = 4

def shrimp_value(shrimp):
    if shrimp == "A": return 1
    if shrimp == "B": return 10
    if shrimp == "C": return 100
    if shrimp == "D": return 1000

@lru_cache(maxsize= 10_000)
def get_all_moves(curr_state):
    all_moves = []
    corridor_blocks = [n for n, item in enumerate(curr_state[0]) if item != "."]
    exit_points = [2, 4, 6, 8]
    for i in range(1, 5):
        moves = 0
        for shrimp in curr_state[i]:
            if shrimp == ".": 
                moves += 1
                continue
            if " ABCD".find(shrimp) == i and not any(x in curr_state[i] for x in "ABCD".replace(shrimp, "")): continue
            a_move = list(curr_state)
            a_move[i] = a_move[i].replace(shrimp, ".", 1)
            exit_point = exit_points[i-1]
            for pos in range(1, exit_point + 1):
                if exit_point - pos in corridor_blocks: break
                elif exit_point - pos < 2 or (exit_point - pos) % 2 == 1:
                    all_moves.append(([a_move[0][:exit_point-pos] + shrimp + a_move[0][exit_point-pos+1:],
                                        a_move[1], a_move[2], a_move[3], a_move[4]], 
                                        (moves + pos + 1) * shrimp_value(shrimp)))
            for pos in range(1, 11 - exit_point):
                if exit_point + pos in corridor_blocks: break
                elif (pos + exit_point) % 2 == 1 or pos + exit_point > 8:
                    all_moves.append(([a_move[0][:exit_point+pos] + shrimp + a_move[0][exit_point+pos+1:],
                                        a_move[1], a_move[2], a_move[3], a_move[4]],
                                        (moves + pos + 1) * shrimp_value(shrimp)))
            break

    for pos, shrimp in enumerate(curr_state[0]):
        moves = 0
        a_move = list(curr_state)
        if shrimp == ".": continue
        else:
            room_index = " ABCD".find(shrimp)
            for other_shrimp in "ABCD".replace(shrimp, ""):
                if other_shrimp in curr_state[room_index]:
                    break
            else:
                if pos < 2 * room_index:
                    for movement in range(pos + 1, 2 * room_index + 1):
                        moves += 1
                        if movement in corridor_blocks: break
                    else:
                        a_move[room_index] = a_move[room_index].replace(".", shrimp, 1)
                        all_moves.append(([a_move[0][:pos] + "." + a_move[0][pos+1:],
                                        a_move[1], a_move[2], a_move[3], a_move[4]],
                                        (moves + a_move[room_index].count(".") + 1) * shrimp_value(shrimp)))
                else:
                    for movement in range(pos - 1, 2 * room_index - 1, -1):
                        moves += 1
                        if movement in corridor_blocks: break
                    else:
                        a_move[room_index] = a_move[room_index].replace(".", shrimp, 1)
                        all_moves.append(([a_move[0][:pos] + "." + a_move[0][pos+1:],
                                        a_move[1], a_move[2], a_move[3], a_move[4]],
                                        (moves + a_move[room_index].count(".") + 1) * shrimp_value(shrimp)))
    return all_moves

def in_order(poss):
    if poss[0] != "...........": return False
    if poss[1] != "A" * room_size: return False
    if poss[2] != "B" * room_size: return False
    if poss[3] != "C" * room_size: return False

    return True

@lru_cache(maxsize= 10_000)
def minimize(position, cost, min_score):

    if cost > min_score: return cost
    if in_order(position) : 
        return cost
    poss_moves = get_all_moves(tuple(position))
    if not poss_moves: return min_score + 1
    for move in poss_moves:
        # print(move)
        score = minimize(tuple(move[0]), cost + move[1], min_score)
        min_score = min(score, min_score)
    
    return min_score

t = time.time()
# starting_pos = ("...........",
#                 "BA", "CD", "BC", "DA")
# room_size = 2
# starting_pos = ("...........",
#                 "BDDA", "CCBD", "BBAC", "DACA")
room_size = 2
starting_pos = ("...........",
                "AC", "DC", "AD", "BB")
print("part 1:", minimize(starting_pos, 0, 99999))
print(time.time() - t)
t = time.time()

room_size = 4
starting_pos = ("...........",
                "ADDC", "DCBC", "ABAD", "BACB")
print("part 2:", minimize(starting_pos, 0, 99999))

print(time.time() - t)