# https://takeuforward.org/data-structure/set-matrix-zero/
# https://leetcode.com/problems/set-matrix-zeroes/
#
#


def setZeroesBruteForce(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def markRow(row):
        for col in range(m):
            if (matrix[row][col]) != 0:
                matrix[row][col] = -1

    def markColumn(col):
        for row in range(n):
            if (matrix[row][col]) != 0:
                matrix[row][col] = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(i)
                markColumn(j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


def setZeroesBetter(matrix):
    n = len(matrix)
    m = len(matrix[0])

    row = [0] * n
    col = [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0


def setZeroesOptimal(matrix):
    # int row[n] = {0}; --> matrix[..][0]
    # int col[m] = {0}; --> matrix[0][..]
    n = len(matrix)
    m = len(matrix[0])

    firstCell = float("inf")

    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0

                if j == 0:
                    firstCell = 0
                else:
                    matrix[0][j] = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    # step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if firstCell == 0:
        for i in range(n):
            matrix[i][0] = 0


if __name__ == "__main__":
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

    matrix = [
        [-4, 9, 1, 3, 2, 11, 6],
        [2, -8, 7, 8, 10, -5, 5],
        [1, 8, -4, 0, 9, 7, -4],
        [1, -7, 11, 5, 0, -4, -6],
        [
            -7,
            4,
            4,
            4,
            2,
            1,
            9,
        ],
        [5, 11, -1, -8, -1, 6, -4],
        [11, -8, -6, 2, 3, 10, 7],
        [
            0,
            1,
            6,
            8,
            3,
            9,
            6,
        ],
        [1, -5, 0, 2, 5, -6, 5],
        [4, 1, 3, -6, 7, 1, -4],
    ]

    print("BEFORE")
    for i in matrix:
        print(str(i), end="\n")

    setZeroesOptimal(matrix)

    print("ANSWER")
    for i in matrix:
        print(str(i), end="\n")
