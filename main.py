# add import statement for your module
from operations import Operation
from Colors import Colors
import os
# Color The Texts

def getMatrix(row=0, col=0):

    row_size = row
    col_size = col

    if row == 0 and col == 0:
        row_size = int(input('row size: ').split()[0])
        col_size = int(input('column size: ').split()[0])


    matrix = [([0] * row_size) for _ in range(col_size)]

    print('Put Numbers in this [{}][{}] Matrix\n'
          '{}(CAUTION: skipping an index means ZERO as the assigned number to that index!){}\n'
          .format(row_size, col_size, Colors.WARNING, Colors.ENDC))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = input('[{}][{}] : '.format(i, j))
            if value == '':
                matrix[i][j] = 0
            else:
                matrix[i][j] = int(value.split()[0])

    return matrix


def transpose():
    makeTranspose = Operation().transpose
    matrix = getMatrix()
    transposed = makeTranspose(matrix)
    print(' -- Transposed -- ')
    Operation().print(transposed)

def subtract():
    matrixOne = getMatrix()

    row = len(matrixOne[0])
    col = len(matrixOne)

    matrixTwo = getMatrix(row, col)

    calcSubtraction = Operation().subtract
    calculated = calcSubtraction(matrixOne, matrixTwo)
    print(' -- Subtraction -- ')
    Operation().print(calculated)

def add():
    matrixOne = getMatrix()

    row = len(matrixOne[0])
    col = len(matrixOne)

    matrixTwo = getMatrix(row, col)

    calcAddition = Operation().add
    calculated = calcAddition(matrixOne, matrixTwo)
    print(' -- Addition -- ')
    Operation().print(calculated)

def multiply():
    matrixOne = getMatrix()

    row = len(matrixOne)
    col = len(matrixOne[0])

    matrixTwo = getMatrix(row, col)

    calcMultiplication = Operation().multiply
    calcMultiplication(matrixOne, matrixTwo)

def showMenu():
    print('1. transpose')
    print('2. subtract')
    print('3. add')
    print('4. multiply')
    print('5. quit')


if __name__ == '__main__':

    quit = False

    while not quit:
        showMenu()
        print('>> ', end='')
        choice = input()

        if choice == '1' or choice.casefold() == 'transpose':
            transpose()
        elif choice == '2' or choice.casefold() == 'subtract':
            subtract()
        elif choice == '3' or choice.casefold() == 'add':
            add()
        elif choice == '4' or choice.casefold() == 'multiply':
            multiply()
        elif choice == '5' or choice.casefold() in ['quit', 'exit']:
            quit = True
        elif choice.casefold() in ['cls', 'clear']:
            os.system('CLS')
        else:
            print('ERROR: INVALID Command!')


0
10
0
12
0
0
0
0
0
0
5
0
15
12
0
0

0
0
8
0
0
0
0
23
0
0
9
0
20
25
0
0
