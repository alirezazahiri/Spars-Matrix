import math

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
        list_to_transpose = self.sparse(matrix)

        # TODO: optimize sorting algo
        # swapped indexes
        for i in range(len(list_to_transpose)):
            for j in range(3):
                list_to_transpose[i][0], list_to_transpose[i][1] = list_to_transpose[i][1], list_to_transpose[i][0]

        # sorting row keys
        for i in range(len(list_to_transpose)):
            for j in range(i, len(list_to_transpose)):
                if list_to_transpose[i][0] > list_to_transpose[j][0]:
                    list_to_transpose[i], list_to_transpose[j] = list_to_transpose[j], list_to_transpose[i]

        # sorting column keys
        for i in range(len(list_to_transpose)):
            for j in range(i, len(list_to_transpose)):
                if list_to_transpose[i][1] > list_to_transpose[j][1] and list_to_transpose[i][0] > list_to_transpose[j][0]:
                    list_to_transpose[i], list_to_transpose[j] = list_to_transpose[j], list_to_transpose[i]

        return self.sort_sparse(list_to_transpose)

    def subtract(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = []

        if len(sparseOne) < len(sparseTwo):
            sparseOne, sparseTwo = sparseTwo, sparseOne

        for i in range(len(sparseTwo)):
            if sparseOne[i][0] == sparseTwo[i][0] and sparseOne[i][1] == sparseTwo[i][1]:
                result.append([sparseTwo[i][0], sparseTwo[i][1], sparseOne[i][2] - sparseTwo[i][2]])
            else:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2]])
                result.append([sparseTwo[i][0], sparseTwo[i][1], sparseTwo[i][2]])

        for i in range(len(sparseTwo), len(sparseOne)):
            if sparseOne[i][0] == sparseTwo[i][0] and sparseOne[i][1] == sparseTwo[i][1]:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2] - sparseTwo[i][2]])
            else:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2]])

        return self.sort_sparse(result)

    def add(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = []

        if len(sparseOne) < len(sparseTwo):
            sparseOne, sparseTwo = sparseTwo, sparseOne

        for i in range(len(sparseTwo)):
            if sparseOne[i][0] == sparseTwo[i][0] and sparseOne[i][1] == sparseTwo[i][1]:
                result.append([sparseTwo[i][0], sparseTwo[i][1], sparseOne[i][2] + sparseTwo[i][2]])
            else:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2]])
                result.append([sparseTwo[i][0], sparseTwo[i][1], sparseTwo[i][2]])

        for i in range(len(sparseTwo), len(sparseOne)):
            if sparseOne[i][0] == sparseTwo[i][0] and sparseOne[i][1] == sparseTwo[i][1]:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2] + sparseTwo[i][2]])
            else:
                result.append([sparseOne[i][0], sparseOne[i][1], sparseOne[i][2]])

        return self.sort_sparse(result)

    def multiply(self, matrixOne: list, matrixTwo: list):
        transposedTwo = self.transpose(matrixTwo)
        matrixTwo = self.de_sparse(transposedTwo, len(matrixTwo), len(matrixTwo[0]))

        # fetch result list
        max_length = len(matrixOne)
        result = [([0] * max_length) for _ in range(max_length)]

        self.print(matrixOne)
        self.print(matrixTwo)

        for i in range(max_length):
            for j in range(max_length):
                for l in range(len(matrixTwo[0])):
                    if matrixOne[i][l] != 0 and matrixTwo[j][l] != 0:
                        result[i][j] += matrixOne[i][l] * matrixTwo[j][l]

        for item in result:
            print(item)

# print(f'result[{i}][{j}] ='
#       f' A[{i}][{l}] * B[{j}][{l}] =='
#       f' {matrixOne[i][l]} * {matrixTwo[j][l]} =='
#       f' {result[i][j] + matrixOne[i][l] * matrixTwo[j][l]}')

        return self.sparse(result)

# result[i][j] = matrixOne[i][?] * matrixTwo[j][?]

    @staticmethod
    def de_sparse(matrix: list, row, col):
        de_sparse_list = [([0] * col) for _ in range(row)]
        for i in range(len(matrix)):
            de_sparse_list[matrix[i][0]][matrix[i][1]] = matrix[i][2]

        return de_sparse_list

    @staticmethod
    def sort_sparse(matrix: list):

        for i in range(len(matrix)-1):
            if matrix[i][0] > matrix[i + 1][0]:
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
            elif matrix[i][0] == matrix[i + 1][0] and matrix[i][1] > matrix[i + 1][1]:
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]

        return matrix

    @staticmethod
    def not_zeros(matrix):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j] == 0:
                    count += 1
        return count

    @staticmethod
    def print(matrix):
        print('{}-- Matrix --{} '.format(Colors.HEADER, Colors.ENDC))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{}{}'.format(Colors.OKCYAN, matrix[i][j]), end=' ')
            print()
        print('{}{}{}'.format(Colors.HEADER, str('-' * 12), Colors.ENDC))
