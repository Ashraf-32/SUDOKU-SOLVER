board = [
    [0, 9, 0, 7, 0, 0, 0, 0, 0],
    [8, 0, 7, 0, 4, 6, 0, 0, 0],
    [6, 1, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 8],
    [0, 4, 0, 0, 2, 0, 0, 0, 9],
    [0, 3, 0, 0, 0, 1, 6, 9, 0],
    [1, 0, 0, 8, 0, 5, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 3, 0],
]


def solution(b):
    get = empty_val(b)
    if not get:
        return True
    else:
        r, c = get

    for i in range(1, 10):
        if checkBoard(b, i, (r, c)):
            b[r][c] = i
            if solution(b):
                return True
            else:
                b[r][c] = 0

    return False


def checkBoard(b, val, cor):
    for i in range(len(b[0])):
        if b[cor[0]][i] == val and cor[1] != i:
            return False

    for i in range(len(b)):
        if b[i][cor[1]] == val and cor[0] != i:
            return False

    x = cor[1] // 3
    y = cor[0] // 3
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if b[i][j] == cor:
                return False

    return True


def display(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("--------------------")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(b[i][j])
            else:
                print(b[i][j], end=" ")


def empty_val(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)

    return None


display(board)
solution(board)
print("THE SODUKO IS SOLVED!!!")
display(board)
