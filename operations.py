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

        return list_to_transpose

    def subtract(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = []

        self.print(sparseOne)
        self.print(sparseTwo)

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

        return result

    def add(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        sparseTwo = self.sparse(matrixTwo)
        result = []

        self.print(sparseOne)
        self.print(sparseTwo)

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

        return result

    def multiply(self, matrixOne: list, matrixTwo: list):
        sparseOne = self.sparse(matrixOne)
        transposedTwo = self.transpose(matrixTwo)

        

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
        print('-- Matrix -- ')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print('{}{}'.format(Colors.OKCYAN, matrix[i][j]), end=' ')
            print('{}'.format(Colors.ENDC))
        print('-' * 12)


