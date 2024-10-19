def is_right_triangle(a, b, c):
    # Sort the sides to identify the longest side
    sides = sorted([a, b, c])
    # Apply the Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Input: lengths of the triangle sides
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# Check if it's a right triangle
if is_right_triangle(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
