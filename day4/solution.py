def sum_board(board):
    s = 0
    for i in board:
        for j in i:
            if not j[1]:
                s += j[0]
    return s


def get_winning_board(boards, callouts):
    for c in callouts:
        for i, board in enumerate(boards):
            for row in board:
                _row = 0
                for itm in row:
                    if itm[0] == c or itm[1]:
                        _row += 1
                        itm[1] = True
                if row[0][0] == c or row[0][1]:
                    row[0][1] = True
                if _row >= 5:
                    return i, c
    return -1, -1


def get_last_winning_board(boards, callouts):
    last = (0, 0)
    wins = 0
    for c in callouts:
        for i, board in enumerate(boards):
            if board != None:
                for j, _ in enumerate(board):
                    _row = 0
                    _col = 0
                    for k in range(5):
                        # Check row
                        if board[j][k][0] == c or board[j][k][1]:
                            _row += 1
                            board[j][k][1] = True
                        # Check column
                        if board[k][j][0] == c or board[k][j][1]:
                            _col += 1
                            board[k][j][1] = True
                    if _row >= 5 or _col >= 5:
                        last = (i, c)
                        wins += 1
                        if wins >= len(boards):
                            return last
                        else:
                            # Remove from boards
                            boards[i] = None
    return last


def part_1():
    # Part one
    with open("data.txt") as file:
        callouts = []
        boards = []
        board = []
        lines = list(map((lambda x: x.split()), file.read().splitlines()))
        # Get all boards, callouts...
        for i, line in enumerate(lines):
            if i == 0:
                callouts = list(
                    map(lambda x: int(x), line[0].split(',')))
            elif line != []:
                board.append(list(map(lambda x: [int(x), False], line)))
            if len(board) >= 5:
                boards.append(board)
                board = []
        b, n = get_winning_board(boards, callouts)
        print(f"part 1 solution = {n * sum_board(boards[b])}")


def part_2():
    # Part one
    with open("data.txt") as file:
        callouts = []
        boards = []
        board = []
        lines = list(map((lambda x: x.split()), file.read().splitlines()))
        # Get all boards, callouts...
        for i, line in enumerate(lines):
            if i == 0:
                callouts = list(
                    map(lambda x: int(x), line[0].split(',')))
            elif line != []:
                board.append(list(map(lambda x: [int(x), False], line)))
            if len(board) >= 5:
                boards.append(board)
                board = []
        b, n = get_last_winning_board(boards, callouts)
        print(f"part 2 solution = {sum_board(boards[b]) * n}")


part_1()
part_2()
