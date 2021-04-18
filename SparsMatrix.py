from Colors import Colors

class SparsMatrix:

    def __init__(self, r, c) -> None:
        self.row = r
        self.col = c
        self.len = 0
        self.data = [([0] * 3) for _ in range(150)]

    def insert(self, r, c, val):
        if r > self.row or c > self.col:
            return
        if val == 0:
            return

        self.data[self.len][0] = r
        self.data[self.len][1] = c
        self.data[self.len][2] = val
        self.len += 1

    def add(self, b):
        if self.row != b.row or self.col != b.col:
            return None

        apos, bpos = 0, 0

        result = SparsMatrix(self.row, self.col)

        while apos < self.len and bpos < b.len:
            if self.data[apos][0] > b.data[bpos][0] or (self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] > b.data[bpos][1]):
                result.insert(b.data[bpos][0], b.data[bpos][1], b.data[bpos][2])
                bpos += 1


            elif self.data[apos][0] < b.data[bpos][0] or (self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] < b.data[bpos][1]):
                result.insert(self.data[apos][0], self.data[apos][1], self.data[apos][2])
                apos += 1

            else:
                addedval = self.data[apos][2] + b.data[bpos][2]

                if addedval != 0:
                    result.insert(self.data[apos][0], self.data[apos][1], addedval)

                apos += 1
                bpos += 1

        while apos < self.len:
            result.insert(self.data[apos][0], self.data[apos][1], self.data[apos][2])
            apos += 1
        while bpos < self.len:
            result.insert(b.data[bpos][0], b.data[bpos][1], b.data[bpos][2])
            bpos += 1

        return result

    def toNegative(self):
        for i in range(self.len):
            self.data[i][2] *= -1

    def subtract(self, b):
        if self.row != b.row or self.col != b.col:
            return None

        b.toNegative()
        result = self.add(b)
        return result

    def transpose(self):
        result = SparsMatrix(self.row, self.col)
        for i in range(self.len):
            result.insert(self.data[i][1], self.data[i][0], self.data[i][2])

        result.mergeSort(0, self.len - 1)
        return result

    def multiply(self, b):
        if self.col != b.row:
            return None

        check = []
        b = b.transpose()
        result = SparsMatrix(self.row, b.row)

        # while apos < self.len:
        for apos in range(self.len):
            r = self.data[apos][0]

            # while bpos < b.len:
            for bpos in range(b.len):
                c = b.data[bpos][0]
                tempa, tempb = apos, bpos
                sum = 0
                while tempa < self.len and self.data[tempa][0] == r and tempb < b.len and b.data[tempb][0] == c:
                    if self.data[tempa][1] < b.data[tempb][1]:
                        tempa += 1
                    elif self.data[tempa][1] > b.data[tempb][1]:
                        tempb += 1
                    else:
                        sum += self.data[tempa][2] * b.data[tempb][2]
                        tempa += 1
                        tempb += 1

                if sum != 0:
                    if [r, c] not in check:
                        check.append([r, c])
                        result.insert(r, c, sum)

                while bpos < b.len and b.data[bpos][0] == c:
                    bpos += 1

            while apos < self.len and self.data[apos][0] == r:
                apos += 1

        return result

    def print(self):
        print(f'{Colors.UNDERLINE}{Colors.FAIL}                      {Colors.ENDC}\n')
        print(f'{Colors.HEADER}RESULT[{self.row}][{self.col}] -> {Colors.ENDC}')

        print('{}{:<6}{:<6}{:<6}{}'.format(Colors.WARNING, 'ROW', 'COL', 'VALUE', Colors.ENDC))
        for i in range(self.len):
            print('{}{:<6}{:<6}{:<6}{}'.format(Colors.OKCYAN, self.data[i][0], self.data[i][1], self.data[i][2], Colors.ENDC))
        print(f'{Colors.UNDERLINE}{Colors.FAIL}                      {Colors.ENDC}')

    def merge(self, l, m, r):
        x = m - l + 1
        y = r - m
        L = [([0] * 3) for _ in range(x)]
        R = [([0] * 3) for _ in range(y)]

        for i in range(x):
            L[i][0] = self.data[l + i][0]
            L[i][1] = self.data[l + i][1]
            L[i][2] = self.data[l + i][2]

        for i in range(y):
            R[i][0] = self.data[m + 1 + i][0]
            R[i][1] = self.data[m + 1 + i][1]
            R[i][2] = self.data[m + 1 + i][2]

        i, j = 0, 0
        index = l

        while i < x and j < y:
            if L[i][0] <= R[j][0] or L[i][0] == R[j][0] and L[i][1] < R[j][1]:
                self.data[index][0] = L[i][0]
                self.data[index][1] = L[i][1]
                self.data[index][2] = L[i][2]
                i += 1
            else:
                self.data[index][0] = R[j][0]
                self.data[index][1] = R[j][1]
                self.data[index][2] = R[j][2]
                j += 1
            index += 1

        while i < x:
            self.data[index][0] = L[i][0]
            self.data[index][1] = L[i][1]
            self.data[index][2] = L[i][2]
            i += 1
            index += 1

        while j < y:
            self.data[index][0] = R[j][0]
            self.data[index][1] = R[j][1]
            self.data[index][2] = R[j][2]
            j += 1
            index += 1

    def mergeSort(self, l, r):
        if r <= l:
            return

        m = (l + r) // 2
        self.mergeSort(l, m)
        self.mergeSort(m+1, r)
        self.merge(l, m, r)

