from operations import Operation
from Colors import Colors
import os

def getMatrix(row=0, col=0):

    row_size = row
    col_size = col

    if row == 0 and col == 0:
        row_size = int(input('row size: ').split()[0])
        col_size = int(input('column size: ').split()[0])


    matrix = [([0] * row_size) for _ in range(col_size)]

    print('Put Numbers in this {}[{}][{}]{} Matrix\n'
          '{}({}CAUTION{}: skipping an index means {}ZERO{} as the assigned number to that index!{}){}\n'
          .format(Colors.WARNING,
                  row_size, col_size,
                  Colors.ENDC,
                  Colors.FAIL,
                  Colors.WARNING, Colors.ENDC,
                  Colors.WARNING, Colors.ENDC,
                  Colors.FAIL, Colors.ENDC))

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
    print('{}Transposed ->{}'.format(Colors.HEADER, Colors.ENDC))
    Operation().print(transposed)

def subtract():
    matrixOne = getMatrix()

    row = len(matrixOne[0])
    col = len(matrixOne)

    matrixTwo = getMatrix(row, col)

    calcSubtraction = Operation().subtract
    calculated = calcSubtraction(matrixOne, matrixTwo)
    print('{}Subtraction ->{}'.format(Colors.HEADER, Colors.ENDC))
    Operation().print(calculated)

def add():
    matrixOne = getMatrix()

    row = len(matrixOne[0])
    col = len(matrixOne)

    matrixTwo = getMatrix(row, col)

    calcAddition = Operation().add
    calculated = calcAddition(matrixOne, matrixTwo)
    print('{}Addition ->{}'.format(Colors.HEADER, Colors.ENDC))
    Operation().print(calculated)

def multiply():
    matrixOne = getMatrix()

    row = len(matrixOne)
    col = len(matrixOne[0])

    matrixTwo = getMatrix(row, col)

    calcMultiplication = Operation().multiply
    calculated = calcMultiplication(matrixOne, matrixTwo)
    print('{}Multiplication ->{}'.format(Colors.HEADER, Colors.ENDC))
    Operation().print(calculated)

def showMenu():
    print('{}{}'.format(Colors.BOLD, Colors.OKBLUE), end='')
    print('1. transpose')
    print('2. subtract')
    print('3. add')
    print('4. multiply')
    print('5. quit')
    print('{}'.format(Colors.ENDC), end='')


if __name__ == '__main__':
    os.system('CLS')
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
            print('{}ERROR: INVALID Command!{}'.format(Colors.FAIL, Colors.ENDC))
