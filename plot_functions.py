import matplotlib.pyplot as plt


def plot_errors(jacobi, gauss):
    iterations_jacobi = [i for i in range(1, jacobi[1] + 1)]
    iterations_gauss = [i for i in range(1, gauss[1] + 1)]
    errors_jacobi = jacobi[3]
    errors_gauss = gauss[3]

    plt.yscale('log')
    plt.plot(iterations_jacobi, errors_jacobi, '')
    plt.plot(iterations_gauss, errors_gauss, '')
    plt.legend(['Jacobi', 'Gauss'])
    plt.xlabel('Iterations')
    plt.ylabel('Error value')
    plt.show()


def plot_times(jacobis, gausses, lus, sizes):
    times_jacobi = [jacobi[2] for jacobi in jacobis]
    times_gauss = [gauss[2] for gauss in gausses]
    times_lu = [lu[1] for lu in lus]

    plt.plot(sizes, times_jacobi, '')
    plt.plot(sizes, times_gauss, '')
    plt.plot(sizes, times_lu, '')
    plt.legend(['Jacobi', 'Gauss', 'LU'])
    plt.xlabel('Sizes')
    plt.ylabel('Time')
    plt.show()

