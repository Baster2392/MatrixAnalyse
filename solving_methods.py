import matrix_functions as mf
from time import *


def jacobi_solving_method(matrix_a, vector_b, iterations, error):
    # initialize matrices
    diagonal = mf.diag(matrix_a)
    lower_triangular = mf.subtract(mf.tril(matrix_a), diagonal)
    upper_triangular = mf.subtract(mf.triu(matrix_a), diagonal)
    inv_diagonal = mf.inverse_diagonal(diagonal)
    x_matrix = mf.generate_vector_x(len(matrix_a), 1)

    L_U_matrix = mf.add(lower_triangular, upper_triangular)
    M_matrix = mf.multiply(inv_diagonal, mf.minus(L_U_matrix))
    N_matrix = mf.multiply(inv_diagonal, vector_b)

    iterations_counter = 0
    start_time = time()
    res = []
    loop = True
    while loop and iterations_counter < iterations:
        new_x_matrix = mf.multiply(M_matrix, x_matrix)
        new_x_matrix = mf.add(new_x_matrix, N_matrix)

        try:
            err_norm = mf.norm_vector(mf.subtract(mf.multiply(matrix_a, new_x_matrix), vector_b))
            res.append(err_norm)
            iterations_counter += 1
            if err_norm <= error:
                loop = False
        except OverflowError:
            loop = False

        x_matrix = new_x_matrix

    running_time = time() - start_time
    return x_matrix, iterations_counter, running_time, res


def gauss_seidel_solving_method(matrix_a, vector_b, iterations, error):
    # initialize matrices
    diagonal = mf.diag(matrix_a)
    lower_triangular = mf.subtract(mf.tril(matrix_a), diagonal)
    upper_triangular = mf.subtract(mf.triu(matrix_a), diagonal)
    x_matrix = mf.generate_vector_x(len(matrix_a), 1)

    D_L_matrix = mf.add(diagonal, lower_triangular)
    D_L_matrix = mf.inverse_lower_triangular(D_L_matrix)
    M_matrix = mf.multiply(D_L_matrix, mf.minus(upper_triangular))
    N_matrix = mf.multiply(D_L_matrix, vector_b)

    iterations_counter = 0
    start_time = time()
    res = []
    loop = True
    while loop and iterations_counter < iterations:
        new_x_matrix = mf.multiply(M_matrix, x_matrix)
        new_x_matrix = mf.add(new_x_matrix, N_matrix)

        try:
            err_norm = mf.norm_vector(mf.subtract(mf.multiply(matrix_a, new_x_matrix), vector_b))
            res.append(err_norm)
            iterations_counter += 1
            if err_norm <= error:
                loop = False
        except OverflowError:
            loop = False

        x_matrix = new_x_matrix

    running_time = time() - start_time
    return x_matrix, iterations_counter, running_time, res


def LU_solving_method(matrix_a, vector_b):
    time_start = time()
    lower, upper = mf.lu_decomposition(matrix_a)
    inv_lower = mf.inverse_lower_triangular(lower)
    inv_upper = mf.inverse_upper_triangular(upper)
    inv_matrix_a = mf.multiply(inv_upper, inv_lower)
    x_vector = mf.multiply(inv_matrix_a, vector_b)
    err_norm = mf.norm_vector(mf.subtract(mf.multiply(matrix_a, x_vector), vector_b))
    running_time = time() - time_start

    return x_vector, running_time, err_norm
