import sympy as sp

def bisection_method(func, a, b, tol=1e-5):
    """Numeric method used to find the root of a function in a closed
    interval [a, b] by iteratively dividing the interval in half. The
    final result will have as much decimal places of accuracy as "tol"
    says.
    Args:
        func (function): The objective function.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for convergence.
        max_iter (int): The maximum number of iterations.
    Returns:
        None
    """
    iter_number = 0
    while True:
        iter_number += 1
        if abs(b-a) <= tol:
            print(f"Root found: {a:.{int(abs(sp.log(tol, 10)))}f}")
            print(f"Achieved on iteration: {iter_number}")
            break
        # Calculate midpoint
        pn = (a + b) / 2

        # Evaluate function at midpoint
        fpn = func.subs(sp.symbols('x'), pn).evalf()

        # Check if there´s a sign change
        if fpn == 0:
            print(f"Root found: {pn:.{int(abs(sp.log(tol, 10)))}f}")
            print(f"Achieved on iteration: {iter_number}")
            break
        elif func.subs(sp.symbols('x'), a).evalf() * fpn < 0:
            b = pn
        else:
            a = pn


def theorical_iter_number(a, b, tol=1e-5):
    """Calculate the theoretical number of iterations needed to find the
    root of a function in a closed interval [a, b] with a given
    tolerance.
    Args:
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for convergence.
    """
    print(
        f"Theoretical number of iterations needed to find the root: {int((sp.ln(b-a) - sp.ln(tol)) / sp.ln(2))+1}"
        )


if __name__ == "__main__":
    # Define the function as a symbolic expression
    x = sp.symbols('x')
    # Define the fuction expression
    func = sp.tan(sp.exp(x))-(x/(x-2))

    # Lower bound
    a = -1.5
    # Upper bound
    b = 0
    # Define the tolerance
    tol = 1e-9

    # Find the root of the function and calculated the number of iterations used
    bisection_method(func, a, b, tol)

    # Calculate the theoretical number of iterations needed to find the root
    theorical_iter_number(a, b, tol)


