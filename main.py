# add import statement for your module

def transpose():
    print('tarnspose fired!')

def subtract():
    print('subtract fired!')

def add():
    print('add fired!')

def multiply():
    print('multiply fired!')


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
        print('>> ')
        choice = input()

        if choice == '1' or choice.casefold() == 'transpose':
            transpose()
        elif choice == '2' or choice.casefold() == 'subtract':
            subtract()
        elif choice == '3' or choice.casefold() == 'add':
            add()
        elif choice == '4' or choice.casefold() == 'multiply':
            multiply()
        elif choice == '5' or choice.casefold() == 'quit':
            quit = True
        else:
            print('ERROR: INVALID Command!')

