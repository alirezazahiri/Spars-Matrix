from Colors import Colors
from SparsMatrix import SparsMatrix
import os

def getMatrix(row=0, col=0):

    row_size = row
    col_size = col

    if row == 0 and col == 0:
        row_size = int(input(f'{Colors.OKGREEN}row size: ').split()[0])
        col_size = int(input('column size: ').split()[0])

    matrix = SparsMatrix(row_size, col_size)

    print('{}\nPut Numbers in this {}[{}][{}]{} Matrix\n'
          '{}({}CAUTION{}: skipping an index means {}ZERO{} as the assigned number to that index!{}){}\n'
          .format(Colors.ENDC, Colors.WARNING,
                  row_size, col_size,
                  Colors.ENDC,
                  Colors.FAIL,
                  Colors.WARNING, Colors.ENDC,
                  Colors.WARNING, Colors.ENDC,
                  Colors.FAIL, Colors.ENDC))

    for i in range(row_size):
        for j in range(col_size):
            value = input('{}[{}][{}] : {}'.format(Colors.OKGREEN, i, j, Colors.ENDC))
            if value == '':
                matrix.insert(i, j, 0)
            else:
                matrix.insert(i, j, int(value.split()[0]))

    return row_size, col_size, matrix

def transpose():
    x, y, matrix = getMatrix()
    matrix.transpose().print()

def subtract():
    x1, y1, matrixOne = getMatrix()

    x2, y2, matrixTwo = getMatrix(x1, y1)

    matrixOne.subtract(matrixTwo).print()

def add():
    x1, y1, matrixOne = getMatrix()

    x2, y2, matrixTwo = getMatrix(x1, y1)

    matrixOne.add(matrixTwo).print()

def multiply():
    x1, y1, matrixOne = getMatrix()
    x2, y2, matrixTwo = getMatrix()

    matrixOne.multiply(matrixTwo).print()


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
