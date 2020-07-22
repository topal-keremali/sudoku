def findNextCellToFill(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x, y
    return -1, -1


def rowOK(board, i, j, e):
    for val in range(9):
        if e == board[i][val]: return False
    return True


def colOK(board, i, j, e):
    for val in range(9):
        if e == board[val][j]: return False
    return True


def isValid(board, i, j, e):
    if rowOK(board, i, j, e):
        if colOK(board, i, j, e):
            sX, sY = 3 * (i // 3), 3 * (j // 3)
            for x in range(sX, sX + 3):
                for y in range(sY, sY + 3):
                    if board[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(board, i=0, j=0):
    i, j = findNextCellToFill(board)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(board, i, j, e):
            board[i][j] = e
            if solveSudoku(board, i, j):
                return True
            board[i][j] = 0
    return False

def printSudoku(feld):
    schoene_zeile= "+-------+-------+-------+"
    sudoku_ausgabe=[]
    for i in range(9):
        if i % 1 == 0:
            sudoku_ausgabe.append('\n')
        if i % 3 == 0:
            sudoku_ausgabe.append(schoene_zeile)
            sudoku_ausgabe.append('\n')
        for j in range(9):
            if j%3==0:
                    sudoku_ausgabe.append('|')
            sudoku_ausgabe.append(feld[i][j])
            if j == 8:
                sudoku_ausgabe.append('|')
                if i==8:
                    sudoku_ausgabe.append('\n')
                    sudoku_ausgabe.append(schoene_zeile)

    ausgabe = " ".join(map(str,sudoku_ausgabe))
    print(ausgabe)

def string_to_board(feld_str):
    k = 0
    feld=[]
    for i in range(9):
        zeile=[]
        for j in range(9):
            char_from_string = int (feld_str[k])
            k=k+1
            zeile.append(char_from_string)
            if j%9==0:
                feld.append(zeile)
    return feld

def sudoku_aus_datei_loesen():
    with open("sudoku-Liste.txt","r") as file:
        for line in file:
            feld_als_string=line
            feld=string_to_board(feld_als_string)
            solveSudoku(feld)
            printSudoku(feld)


sudoku_aus_datei_loesen()





