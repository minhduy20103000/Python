# Function to find the largest number
def find_largest(numbers):
    return max(numbers)

# Function to find the smallest number
def find_smallest(numbers):
    return min(numbers)

# Main function
def main():
    # Prompt the user to enter four numbers
    numbers = []
    for i in range(4):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Get user preference for largest or smallest
    choice = input("Do you want to find the largest or smallest number? (Enter 'largest' or 'smallest'): ").strip().lower()

    if choice == 'largest':
        result = find_largest(numbers)
        print(f"The largest number among {numbers} is: {result}")
    elif choice == 'smallest':
        result = find_smallest(numbers)
        print(f"The smallest number among {numbers} is: {result}")
    else:
        print("Invalid choice. Please enter 'largest' or 'smallest'.")

# Run the program
if __name__ == "__main__":
    main()
