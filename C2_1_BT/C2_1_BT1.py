def calculate_bmi(w, h):
    bmi = w / (h**2)
    return bmi

def bmi_c(bmi):
    if bmi < 18.5:
        return "Watch out for the wind"
    elif 18.5 <= bmi < 25:
        return "Standard model"
    else:
        return "A little fat"

def main():
    w = float(input("Weight (kg): "))
    h = float(input("Height (m): "))
    bmi = calculate_bmi(w, h)
    c = bmi_c(bmi)
    
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {c}")

if __name__ == "__main__":
    main()
