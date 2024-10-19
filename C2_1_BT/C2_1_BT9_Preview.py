import math

def solve_quadratic(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "The equation has countless solutions."
    elif a == 0 and b == 0:
        return "The equation has no solutions."
    elif a == 0:
        return f"The equation has a solution: x = {-c / b}"
    else:
        delta = b**2 - 4*a*c
        
        if delta < 0:
            return "The equation has no solutions."
        elif delta == 0:
            x = -b / (2 * a)
            return f"The equation has a double solution: x = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"The equation has two solutions: x1 = {x1}, x2 = {x2}"

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve_quadratic(a, b, c)
print(result)
