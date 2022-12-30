moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def search(matrix, pos):
    return matrix[pos[0]][pos[1]]

def make_move(pos, maze, teleport, move, amount):
    i = 0
    while i < amount:
        pos = add(pos, move)
        i += 1

        if not (obstacle := search(maze, pos)):
            return (pos[0] - move[0], pos[1] - move[1]), move

        if obstacle == 2:
            teleport_pos, new_move = teleport[(pos, move)]
            if not search(maze, teleport_pos):
                return (pos[0] - move[0], pos[1] - move[1]), move
            pos = teleport_pos
            move = new_move
            

    return pos, move


def main():
    lines = open("input.txt").readlines()
    movement = lines[-1].strip()

    maze = []
    teleport = {}
    max_size = 0
    for line in lines[:-2]:
        row = [2]
        for char in line:
            if char == " ":
                row.append(2)
            elif char == ".":
                row.append(1)
            elif char == "#":
                row.append(0)
            else:
                row.append(2)
        max_size = max(max_size, len(row))
        k = max_size - len(row)
        row += [2] * k
        maze.append(row)
    
    maze = [[2] * len(maze[0])] + maze + [[2] * len(maze[-1])]
    teleport = {}


    for i in range(1, 51):
        teleport[((0, i + 50), (-1, 0))] = ((i + 150, 1), (0, 1)) # 0 up -> 5 left
        teleport[((i, 50), (0, -1))] = ((151 - i, 1), (0, 1)) # 0 left -> 3 left inv
        teleport[((0, i + 100), (-1, 0))] = ((200, i), (-1, 0)) # 1 up -> 5 down
        teleport[((51, i + 100), (1, 0))] = ((i + 50, 100), (0, -1)) # 1 down -> 2 right
        teleport[((i, 151), (0, 1))] = ((151 - i, 100), (0, -1)) # 1 right -> 4 right inv
        teleport[((i + 50, 50), (0, -1))] = ((101, i), (1, 0)) # 2 left -> 3 up
        teleport[((i + 50, 101), (0, 1))] = ((50, 100 + i), (-1, 0)) # 2 right -> 1 down 
        teleport[((100, i), (-1, 0))] = ((i + 50, 51), (0, 1)) # 3 up -> 2 left
        teleport[((i + 100, 0), (0, -1))] = ((51 - i, 51), (0, 1)) # 3 left -> 0 left inv
        teleport[((100 + i, 101), (0, 1))] = ((51 - i, 150), (0, -1)) # 4 right -> 1 right inv
        teleport[((151, i + 50), (1, 0))] = ((i + 150, 50), (0, -1)) # 4 down -> 5 right 
        teleport[((150 + i, 0), (0, -1))] = ((1, 50 + i), (1, 0)) # 5 left -> 0 up
        teleport[((150 + i, 51), (0, 1))] = ((150, 50 + i), (-1, 0)) # 5 right -> 4 down
        teleport[((201, i), (1, 0))] = ((1, 100 + i), (1, 0)) # 5 down -> 1 up


    pos = (1, 51)

    num = ""
    move_id = 0
    move = moves[0]
    for char in movement.strip():
        if not char in ("R", "L"):
            num += char
            continue
        
        pos, move = make_move(pos, maze, teleport, move, int(num))


        move_id = moves.index(move)
        move_id += 1 if char == "R" else -1

        move = moves[move_id % 4]
        num = ""
    
    pos, move = make_move(pos, maze, teleport, move, int(num))
    move_id = moves.index(move)
    print(pos)
    print(pos[0] * 1000 + pos[1] * 4 + move_id % 4)
        
    

if __name__ == "__main__":
    main()
