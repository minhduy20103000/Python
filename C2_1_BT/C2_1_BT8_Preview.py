def solve_equation():
    # Input coefficients a and b from the user
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    
    # Determine the type of solution
    if a != 0:
        # Calculate the solution x = -b/a
        x = -b / a
        print(f"The solution is: x = {x}")
    elif a == 0 and b == 0:
        # Infinite solutions
        print("The equation has infinite solutions.")
    else:  # a == 0 and b != 0
        # No solutions
        print("The equation has no solutions.")

# Call the function to execute
solve_equation()
