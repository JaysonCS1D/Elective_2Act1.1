import math
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# BISECTION METHOD
# ---------------------------------------------------------
def bisection(f, a, b, decimals=6):
    """
    Finds a root of f(x) using the Bisection Method.

    a and b must bracket a root:
        f(a) and f(b) must have opposite signs,
        unless a or b is already an exact root.
    """
    tolerance = 0.5 * 10 ** (-decimals)

    fa = f(a)
    fb = f(b)

    # Check if an endpoint is already a root.
    if abs(fa) < 1e-15:
        return a
    if abs(fb) < 1e-15:
        return b

    if fa * fb > 0:
        raise ValueError(
            f"No sign change on [{a}, {b}]. "
            "Choose an interval that brackets a root."
        )

    iterations = 0

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        fc = f(c)
        iterations += 1

        # If the midpoint is the root.
        if abs(fc) < 1e-15:
            return c

        # Keep the half containing the sign change.
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2


# ---------------------------------------------------------
# FUNCTION DEFINITIONS
# The equations are rewritten as f(x) = 0.
# ---------------------------------------------------------

# Problem 1
f1a = lambda x: x**3 - 9
f1b = lambda x: 3*x**3 + x**2 - x - 5
f1c = lambda x: math.cos(x)**2 + 6 - x

# Problem 2
f2a = lambda x: x**5 + x - 1
f2b = lambda x: math.sin(x) - 6*x - 5
f2c = lambda x: math.log(x) + x**2 - 3

# Problem 3
f3a = lambda x: 2*x**3 - 6*x - 1
f3b = lambda x: math.exp(x - 2) + x**3 - x
f3c = lambda x: 1 + 5*x - 6*x**3 - math.exp(2*x)


# ---------------------------------------------------------
# PROBLEM 1
# Find each root to 6 correct decimal places.
# ---------------------------------------------------------
def problem_1():
    print("\n" + "=" * 65)
    print("PROBLEM 1 - Bisection Method, 6 Decimal Places")
    print("=" * 65)

    questions = [
        ("1(a): x^3 = 9", f1a, 2, 3),
        ("1(b): 3x^3 + x^2 = x + 5", f1b, 1, 2),
        ("1(c): cos^2(x) + 6 = x", f1c, 6, 7),
    ]

    for name, f, a, b in questions:
        root = bisection(f, a, b, decimals=6)
        print(f"{name}")
        print(f"  Interval: [{a}, {b}]")
        print(f"  Root:     {root:.6f}")
        print(f"  f(root):  {f(root):.10f}")
        print()


# ---------------------------------------------------------
# PROBLEM 2
# Find each root to 8 correct decimal places.
# ---------------------------------------------------------
def problem_2():
    print("\n" + "=" * 65)
    print("PROBLEM 2 - Bisection Method, 8 Decimal Places")
    print("=" * 65)

    questions = [
        ("2(a): x^5 + x = 1", f2a, 0, 1),
        ("2(b): sin(x) = 6x + 5", f2b, -1, 0),
        ("2(c): ln(x) + x^2 = 3", f2c, 1, 2),
    ]

    for name, f, a, b in questions:
        root = bisection(f, a, b, decimals=8)
        print(f"{name}")
        print(f"  Interval: [{a}, {b}]")
        print(f"  Root:     {root:.8f}")
        print(f"  f(root):  {f(root):.10f}")
        print()


# ---------------------------------------------------------
# PROBLEM 3
# Locate all roots, show three intervals of length 1,
# sketch the functions, and find the roots to 6 decimals.
# ---------------------------------------------------------
def problem_3():
    print("\n" + "=" * 65)
    print("PROBLEM 3 - All Solutions")
    print("=" * 65)

    # These are three length-1 intervals for each equation.
    # Each interval contains one of the roots.
    equations = [
        (
            "3(a): 2x^3 - 6x - 1 = 0",
            f3a,
            [(-2, -1), (-1, 0), (1, 2)],
            (-3, 3)
        ),
        (
            "3(b): e^(x-2) + x^3 - x = 0",
            f3b,
            [(-2, -1), (-0.3, 0.7), (0.5, 1.5)],
            (-3, 3)
        ),
        (
            "3(c): 1 + 5x - 6x^3 - e^(2x) = 0",
            f3c,
            [(-1, 0), (-0.5, 0.5), (0.5, 1.5)],
            (-2, 2)
        ),
    ]

    for name, f, intervals, plot_range in equations:
        print(f"\n{name}")
        print("Length-1 intervals and roots:")

        for a, b in intervals:
            root = bisection(f, a, b, decimals=6)
            print(
                f"  [{a:5.2f}, {b:5.2f}]  "
                f"-> root = {root:.6f}"
            )

        # Sketch the function using Python/Matplotlib.
        x_min, x_max = plot_range
        x_values = []
        y_values = []

        # Avoid invalid values if a function has a restricted domain.
        for i in range(1001):
            x = x_min + (x_max - x_min) * i / 1000
            try:
                y = f(x)
                if math.isfinite(y):
                    x_values.append(x)
                    y_values.append(y)
            except (ValueError, OverflowError):
                pass

        plt.figure(figsize=(8, 5))
        plt.plot(x_values, y_values, label=name)
        plt.axhline(0, linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(name)
        plt.grid(True)
        plt.legend()
        plt.show()


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():
    while True:
        print("\n" + "=" * 65)
        print("BISECTION METHOD - ACTIVITY 1.1")
        print("=" * 65)
        print("1. Solve Problem 1")
        print("2. Solve Problem 2")
        print("3. Solve Problem 3")
        print("4. Solve Problems 1, 2, and 3")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "3":
            problem_3()
        elif choice == "4":
            problem_1()
            problem_2()
            problem_3()
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
