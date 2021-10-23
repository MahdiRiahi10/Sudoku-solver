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

def checkBlock (number, board, rowIndex, columnIndex):
    borders = getBlockBorders(rowIndex, columnIndex)
    for row in range(borders['startRow'], borders['endRow'] + 1):
        for column in range(borders['startColumn'], borders['endColumn'] + 1):
           if row != rowIndex  and column != columnIndex:
               if number == board[row][column]:
                   return False
    return True

def checkRow (number, rowIndex, index):
    for cellIndex, cell in enumerate(board[rowIndex]):
        if cellIndex != index:
            if cell == number:
                return False
    return True

def checkColumn(number, board, rowIndex, columnIndex):
    for index, row in enumerate(board):
        if index != rowIndex:
            if row[columnIndex] == number:
                return False
    return True

from random import randrange

def getProposition(board, rowIndex, columnIndex):
    triedNumbers = []
    while True:
        if len(triedNumbers) == 9:
            return 0
        number = randrange(1, 10)
        print(number)
        if checkRow(number, rowIndex, columnIndex) and checkColumn(number, board, rowIndex, columnIndex) and checkBlock(number, board, rowIndex, columnIndex):
            return number
        else:
            if number not in triedNumbers:
                triedNumbers.append(number)

def backTrack(board, originalBoard, rowIndex, borders):
    for index in range(borders['startColumn'], borders['endColumn'] + 1):
        board[rowIndex][index] = originalBoard[rowIndex][index]
    return board 

import copy

def solveBoard(board):
    count = 0
    rowIndex = -1
    originalBoard = copy.deepcopy(board)
    while rowIndex < len(board):
        rowIndex += 1
        columnIndex = 0
        backTrackTimes = 0
        rowFailurePos = -1
        colFailurePos = -1
        while columnIndex < len(board[rowIndex]):   
            if board[rowIndex][columnIndex] == 0:
                count += 1  
                x = getProposition(board, rowIndex, columnIndex)

                if x == 0:
                    ## In case it fails again after backtracking in another cell placed before the first cell failure so we should ignore the first
                    if colFailurePos != columnIndex or rowFailurePos != rowIndex:
                        backTrackTimes = 0
                    backTrackTimes += 1
                    rowFailurePos = rowIndex
                    colFailurePos = columnIndex
                    startColumn = columnIndex
                    for i in range(backTrackTimes):
                        borders = getBlockBorders(rowIndex, startColumn)
                        startColumn = borders['startColumn'] - 1
                        board = backTrack(board, originalBoard, rowIndex, borders)
                    columnIndex = borders['startColumn']
                else:
                    board[rowIndex][columnIndex] = x
                    if rowIndex == rowFailurePos and columnIndex == colFailurePos:
                        backTrackTimes = 0
                        rowFailurePos = -1
                        colFailurePos = -1
                    columnIndex += 1
                print("Tentative " + str(count))
                printBoard(board)
            else:
                columnIndex += 1
           
printBoard(board)

solveBoard(board)

print("Done")
