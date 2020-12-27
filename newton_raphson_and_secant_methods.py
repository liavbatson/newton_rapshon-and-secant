def newton_raphson(func, d_fucn, x, tolerence, max_iterations, real_root=None):

    if d_fucn(x) == 0:
        print("Newton-Raphson method will fail.")
        return None
    else:
        iterations = 1
        while abs(func(x) / d_fucn(x)) >= tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            if func(x) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(x))
                return x
            x = x - func(x) / d_fucn(x)
            if d_fucn(x) == 0:
                print("Newton-Raphson method will fail.")
                return None
            current_iteration_print += ", {0}".format(x)
            iterations = iterations + 1
            print(current_iteration_print)

        print("Final Solution:",x)
        print("number of iterations to find solution:",iterations)

def secant(func, lower, upper, tolerance, max_iterations, real_root=None):

    if func(lower) * func(upper) >= 0:
        print("Secant method will fail.")
        return None
    else:
        iterations = 1
        while abs(upper - lower) > tolerance and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            next_point = upper - (func(upper) * (upper - lower)) / (func(upper) - func(lower))
            if func(next_point) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(next_point))
                return next_point
            lower = upper
            upper = next_point
            current_iteration_print += ", {0}".format(next_point)
            iterations = iterations + 1
            print(current_iteration_print)

        print("Final Solution:",next_point)
        print("number of iterations to find solution:", iterations)

def f1(x):
    return x ** 2 - 20

def df1(x):
    return 2 * x

print(secant(f1, 3, 5, 0.00001, 20, 30))

print(newton_raphson(f1, df1, 1.5, 0.00001, 30, 1))