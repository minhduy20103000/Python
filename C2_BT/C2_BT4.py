import math

def calculate_square_root_of_difference():
    try:
        n1 = float(input("First: "))
        n2 = float(input("Second: "))
        d = n1 - n2

        if d < 0:
            print("Error")
        else:
            print(math.sqrt(d))
    except ValueError:
        print("Error")

calculate_square_root_of_difference()
