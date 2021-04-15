from Colors import Colors
class Operation(object):

    def __init__(self) -> None:
        super().__init__()

    def transpose(self, matrix):
        self.print(matrix)
        pass

    def print(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{}{}'.format(Colors.OKCYAN, matrix[i][j]), end=' ')
            print('{}'.format(Colors.ENDC))

