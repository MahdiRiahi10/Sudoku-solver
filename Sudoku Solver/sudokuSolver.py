board = [
    [0, 0, 0, 8, 0, 7, 4, 0, 0],
    [0, 5, 8, 0, 4, 1, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 2],
    [5, 3, 2, 6, 0, 8, 9, 4, 0],
    [4, 8, 0, 1, 2, 9, 3, 7, 0],
    [0, 0, 0, 0, 5, 0, 2, 6, 0],
    [0, 2, 7, 9, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 1, 0, 8, 0, 0],
    [8, 6, 0, 0, 0, 0, 5, 0, 9]
]




def insertBorders(board):
    borderList = ['-'] * len(board)
    resultList = []
    count = 0
    for row in board:
        resultList.append(row)
        count += 1
        if count == 3:
            resultList.append(borderList)
            count = 0
        
    resultList.insert(0, borderList)
    return resultList

def printBoard (board):
    spacing ="    "
    board = insertBorders(board)
    for row in board:
        print("|", end=" ")
        for columnCount, column in enumerate(row + ["|"]):
            indent = spacing
            if (columnCount + 1)%3 == 0:
                indent = " "
            if (columnCount % 3 == 0 and columnCount != 0 and columnCount != len(row)):
                print("|", end=" ")
            
            print(column if column != 0 else " ", end=indent)
        print("\n")

def getBlockBorders(rowIndex, columnIndex):
    borders = {}
    if rowIndex <= 2:
        borders['startRow'] = 0
        borders['endRow'] = 2
    elif rowIndex > 2 and rowIndex <= 5:
        borders['startRow'] = 3
        borders['endRow'] = 5
    else:
        borders['startRow'] = 6
        borders['endRow'] = 8
    
    if columnIndex <= 2:
        borders['startColumn'] = 0
        borders['endColumn'] = 2
    elif columnIndex > 2 and columnIndex <= 5:
        borders['startColumn'] = 3
        borders['endColumn'] = 5
    else:
        borders['startColumn'] = 6
        borders['endColumn'] = 8

    return borders

def checkBlock (number, board, cell):
    borders = getBlockBorders(cell[0], cell[1])
    for row in range(borders['startRow'], borders['endRow'] + 1):
        for column in range(borders['startColumn'], borders['endColumn'] + 1):
           if row != cell[0]  and column != cell[1]:
               if number == board[row][column]:
                   return False
    return True

def checkRow (number, cell):
    for cellIndex, value in enumerate(board[cell[0]]):
        if cellIndex != cell[1]:
            if value == number:
                return False
    return True

def checkColumn(number, board, cell):
    for index, row in enumerate(board):
        if index != cell[0]:
            if row[cell[1]] == number:
                return False
    return True

def validInsertion (board, number, cell):
    if checkColumn(number, board, cell) and checkRow(number, cell) and checkBlock(number, board, cell):
        return True
    return False

def findEmptyCell (board):
    for rowCount, row in enumerate(board):
        for columnCount, cell in enumerate(row):
            if cell == 0:
                return rowCount, columnCount
    return None, None

def solveBoard (board):
    row, column = findEmptyCell (board)
    if row is None:
        return True
    else:
        
        for number in range(1, 10):
            if validInsertion(board, number, (row, column)):
                board[row][column] = number

                printBoard(board)

                if solveBoard(board):
                    return True
                
                board[row][column] = 0
        return False


printBoard(board)

solveBoard(board)

print("Done")