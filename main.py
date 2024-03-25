import matrix_functions as mf

index_number = "193271"
matrix_size = 900 + int(index_number[-2]) * 10 + int(index_number[-1])

if __name__ == '__main__':
    matrix1 = mf.generate_band_matrix(7, 5 + int(index_number[-3]), -1, -1)
    matrix2 = mf.generate_band_matrix(7, 5 + int(index_number[-1]), 2, 3)
    vector = mf.generate_vector_b(7, 2)
    res = mf.multiply(matrix1, matrix2)
    mf.print_matrix(mf.tril(res))


