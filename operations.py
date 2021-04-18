from Colors import Colors

class Operation(object):

    def __init__(self) -> None:
        super().__init__()

    def sparse(self, matrix):
        count_of_numbers = self.not_zeros(matrix)
        sparse_matrix = [[0, 0, 0] for _ in range(count_of_numbers)]

        row = 0
        col = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j] == 0:
                    sparse_matrix[row][col] = i
                    sparse_matrix[row][col+1] = j
                    sparse_matrix[row][col+2] = matrix[i][j]
                    row += 1

        return sparse_matrix

    def transpose(self, matrix):
        self.print(matrix)
        list_to_transpose = self.sparse(matrix)
        self.print(list_to_transpose)

        # TODO: optimize sorting algo
        # swapped indexes
        for i in range(len(list_to_transpose)):
            list_to_transpose[i][0], list_to_transpose[i][1] = list_to_transpose[i][1], list_to_transpose[i][0]

        de_sparse_list = self.de_sparse(list_to_transpose, len(matrix), len(matrix[0]))

        return self.sparse(de_sparse_list)

    def subtract(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = [([0] * len(matrixOne)) for _ in range(len(matrixOne))]

        self.print(sparseOne)
        self.print(sparseTwo)

        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] += matrixOne[i][j] - matrixTwo[i][j]

        return self.sparse(result)

    def add(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = [([0] * len(matrixOne)) for _ in range(len(matrixOne))]

        self.print(sparseOne)
        self.print(sparseTwo)

        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] += matrixOne[i][j] + matrixTwo[i][j]

        return self.sparse(result)

    def multiply(self, matrixOne: list, matrixTwo: list):
        transposedTwo = self.transpose(matrixTwo)
        matrixTwo = self.de_sparse(transposedTwo, len(matrixTwo), len(matrixTwo[0]))

        self.print(transposedTwo)
        self.print(self.sparse(matrixOne))

        # fetch result list
        max_length = len(matrixOne)
        result = [([0] * max_length) for _ in range(max_length)]

        for i in range(max_length):
            for j in range(max_length):
                for l in range(len(matrixTwo[0])):
                    if matrixOne[i][l] != 0 and matrixTwo[j][l] != 0:
                        result[i][j] += matrixOne[i][l] * matrixTwo[j][l]

        return self.sparse(result)

    @staticmethod
    def de_sparse(matrix: list, row, col):
        de_sparse_list = [([0] * col) for _ in range(row)]
        for i in range(len(matrix)):
            de_sparse_list[matrix[i][0]][matrix[i][1]] = matrix[i][2]

        return de_sparse_list

    @staticmethod
    def not_zeros(matrix):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j] == 0:
                    count += 1
        return count

    @staticmethod
    def print(matrix: list):
        print('{}-- Matrix --{} '.format(Colors.HEADER, Colors.ENDC))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{}{}'.format(Colors.OKCYAN, matrix[i][j]), end=' ')
            print()
        print('{}{}{}'.format(Colors.HEADER, str('-' * 12), Colors.ENDC))

