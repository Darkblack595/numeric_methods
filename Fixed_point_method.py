import sympy as sp


def fixed_point_method(func, x0, k, tol=1e-5):
    """Find the fixed point of a function in a given interval,
    this method use a sucesion that converges to cero while 
    the function is continuous in the interval [a, b] and the
    range of the function is contained in [a, b] too. Make sure
    too that the derivate in the interval can be bounded beetwen
    -1 and 1(exclusive).
    Args:
        func (sympy expression): The function to find the fixed point 
        of.
        x0 (float): The initial guess for the fixed point.
        tol (float): The tolerance for convergence.
    Returns:
        None : The function prints the fixed point and the number of 
        iterations.
    """
    # Define a iteration counter
    iter_number = 0

    while True:
        # Plus one more iteration
        iter_number += 1

        # Calculate the next point in the iteration
        x1 = func.subs(sp.symbols('x'), x0).evalf()

        # Calculate the bound and verify if we achieve the tolerance
        if abs(x1 - x0) <= tol:
            print(f"Fixed point found: {x1:.{int(abs(sp.log(tol, 10)))}f}")
            print(f"Achieved on iteration: {iter_number}")
            break

        # Replace the current point with the next point
        x0 = x1


def theorical_iter_number(x0, a, b, k, tol=1e-5):
    """Calculate the theoretical number of iterations needed to find the
    fixed point of a function in a closed interval [a, b] with a given
    tolerance.
    Args:
        x0 (float): The initial guess for the fixed point.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        k (float): The constant that bounds the derivate of the function.
        tol (float): The tolerance for convergence.
    """
    M = max(b-x0, x0-a)
    n = int(sp.ln(M*tol) / sp.ln(k))
    print(
        f"Theoretical number of iterations needed to find the fixed point: {n}"
        )


if __name__ == "__main__":
    """Before running the code, make sure to have sympy installed.
    Make sure to use a continuos function in the interval [a, b] and
    it´s range is contained in the interval too. The function derivate
    must be bounded beetwen -1 and 1(exclusive).
    """
    # Define the function as a symbolic expression
    x = sp.symbols('x')

    # Define the fuction expression
    func = (1+x)**(1/2)

    # Lower bound
    a = 1

    # Upper bound
    b = 2

    # Initial guess
    x0 = 3/2

    # Define the tolerance
    tol = 1e-5

    # Number beetwen 0 and 1(exclusive) that bounds the derivate of the function
    k = (2**(1/2))/4

    # Find the fixed point of the function and calculated the number of iterations used
    fixed_point_method(func, x0, k, tol)

    # Calculate the theoretical number of iterations needed to find the fixed point
    theorical_iter_number(x0, a, b, k, tol)
