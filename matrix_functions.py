import math


def generate_matrix(s1, s2):
    new_matrix = []
    for i in range(s1):
        new_matrix.append([0 for _ in range(s2)])
    return new_matrix


def generate_matrix_with_value(s1, s2, v):
    new_matrix = []
    for i in range(s1):
        new_matrix.append([v for _ in range(s2)])
    return new_matrix


def generate_band_matrix(size, v1, v2, v3):
    band_matrix = generate_matrix(size, size)

    # fill middle diagonal
    for i in range(size):
        band_matrix[i][i] = v1

    # fill second diagonals
    for i in range(0, size - 1):
        band_matrix[i][i + 1] = v2
        band_matrix[i + 1][i] = v2

    # fill third diagonal
    for i in range(0, size - 2):
        band_matrix[i][i + 2] = v3
        band_matrix[i + 2][i] = v3

    return band_matrix


def generate_vector_b(size, f):
    vector = []
    for i in range(size):
        vector.append([math.sin((i + 1) * (f + 1))])
    return vector


def multiply(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError('Matrices must have compatible sizes.')

    result_matrix = generate_matrix(len(m1), len(m2[0]))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            res = 0
            for k in range(len(m1[0])):
                res += m1[i][k] * m2[k][j]
            result_matrix[i][j] = res
    return result_matrix


def tril(matrix):
    if len(matrix[0]) != len(matrix):
        raise ValueError('Matrix is not square.')

    result_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(i + 1):
            result_matrix[i][j] = matrix[i][j]
    return result_matrix


def triu(matrix):
    if len(matrix[0]) != len(matrix):
        raise ValueError('Matrix is not square.')

    result_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            result_matrix[i][j] = matrix[i][j]
    return result_matrix


def diag(matrix):
    if len(matrix[0]) != len(matrix):
        raise ValueError('Matrix is not square.')

    result_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        result_matrix[i][i] = matrix[i][i]
    return result_matrix


def add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same sizes.")

    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix


def subtract(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same sizes.")

    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]

    return result_matrix


def inverse_diagonal(matrix):
    length = len(matrix)
    result_matrix = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(len(matrix)):
        result_matrix[i][length - i - 1] = matrix[i][i]
    return result_matrix


def minus(matrix):
    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[i][j] = -matrix[i][j]
    return result_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)
