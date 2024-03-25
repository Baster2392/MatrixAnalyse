import matrix_functions as mf


def jacobi_solving_method(matrix_a, vector_b):
    diagonal = mf.diag(matrix_a)
    lower_triangular = mf.tril(matrix_a)
    upper_triangular = mf.tril(matrix_a)
    matrix_m = mf.multiply(mf.minus(mf.inverse_diagonal(diagonal)), mf.add(lower_triangular, upper_triangular))

