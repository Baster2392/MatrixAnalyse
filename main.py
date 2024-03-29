import matrix_functions as mf
import solving_methods as sm
import plot_functions as pf

index_number = "193271"
matrix_size = 900 + int(index_number[-2]) * 10 + int(index_number[-1])
error = 1e-9
max_iterations = 1000

test_size = matrix_size

if __name__ == '__main__':
    matrix1 = mf.generate_band_matrix(test_size, 10 + int(index_number[-3]), -1, -1)
    vector = mf.generate_vector_b(test_size, 2)
    """
    solve_jacobi = sm.jacobi_solving_method(matrix1, vector, max_iterations, error)
    solve_gauss = sm.gauss_seidel_solving_method(matrix1, vector, matrix_size, error)
    
        # Ex B
        print("Jacobi:")
        mf.print_matrix(solve_jacobi)
        print("Gauss:")
        mf.print_matrix(solve_gauss)
    
        pf.plot_errors(solve_jacobi, solve_gauss)
    
        # Ex C
        matrix1 = mf.generate_band_matrix(test_size, 3, -1, -1)
        solve_jacobi = sm.jacobi_solving_method(matrix1, vector, max_iterations, error)
        solve_gauss = sm.gauss_seidel_solving_method(matrix1, vector, matrix_size, error)
        pf.plot_errors(solve_jacobi, solve_gauss)
    
        # Ex D
        solve_LU = sm.LU_solving_method(matrix1, vector)
        print("LU")
        print("X", solve_LU[0])
        print("Time", solve_LU[1])
        print("Error", solve_LU[2])
    """

    sizes = [10, 50, 100, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 2000]
    jacobis = []
    gausses = []
    lus = []
    i = 0
    for size in sizes:
        matrix1 = mf.generate_band_matrix(size, 10 + int(index_number[-3]), -1, -1)
        vector = mf.generate_vector_b(size, 2)
        jac = sm.jacobi_solving_method(matrix1, vector, max_iterations, error)
        gau = sm.gauss_seidel_solving_method(matrix1, vector, max_iterations, error)
        lu = sm.LU_solving_method(matrix1, vector)

        jacobis.append(jac)
        gausses.append(gau)
        lus.append(lu)
        i += 1
        pf.plot_times(jacobis, gausses, lus, sizes[:i])
