boards = []

class Board():
    def __init__(self, board) -> None:
        self.board = self.clean_board(board)
        print(self.board)
        self.check_table = [[False for i in range(len(board[0]))] for j in range(len(board))]
    
    def update(self, num):
        for row in self.board:
            if num in row:
                self.check_table[self.board.index(row)][row.index(num)] = True
                # print(self.board[self.board.index(row)][row.index(num)])
    
    def check_win(self):
        for row in self.check_table:
            if all(row): 
                # print(self.check_table, self.board[self.check_table.index(row)])
                return True
        for i in range(len(self.check_table[0])):
            if all([self.check_table[j][i] for j in range(len(self.check_table[i]))]):
                # print(self.check_table)
                # print([self.check_table[j][i] for j in range(len(self.check_table[i]))])
                return True
        else: return False
    
    def clean_board(self, board):
        for row_num, row in enumerate(board):
            board[row_num] = row.strip("\n")
            board[row_num] = board[row_num].split(" ")
        return board 

def find_score(board, num):
    sum = 0
    for row1, row2 in zip(board.board, board.check_table):
        for n, is_checked in zip(row1, row2):
            if not is_checked:
                sum += int(n)
    return sum * num

with open ("4/inputs.txt") as f:
    draws = f.readline()
    temp_board = []
    n = 0
    for line in f:
        if line == "\n": continue
        temp_board.append(line)
        n += 1
        if n % 5 == 0:
            boards.append(Board(temp_board))
            temp_board = []

draws = draws.strip("\n")
draws = draws.split(",")

print(len(boards))

for num in draws:
    print("num is ", num)
    for board in boards:
        board.update(num)
        if board.check_win(): 
            print(find_score(board, int(num)))
            break
    else: continue
    break
else: print("no winners")
