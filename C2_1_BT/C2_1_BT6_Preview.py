def classify_triangle(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    
    # Classify the triangle
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    print("Enter the lengths of the three sides of the triangle:")
    try:
        a = float(input("Side 1: "))
        b = float(input("Side 2: "))
        c = float(input("Side 3: "))
        
        triangle_type = classify_triangle(a, b, c)
        print(f"The triangle is: {triangle_type}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
