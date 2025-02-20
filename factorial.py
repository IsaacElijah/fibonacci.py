def calculate_factorial(n):
    """Calculate factorial of a number using a loop"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    """Main function to interact with the user and calculate factorial"""
    print()
    print("Welcome to the Factorial Calculator!")
    print()

    while True:
        try:
            n = int(input("Enter a non-negative integer to calculate its factorial: "))
            if n < 0:
                print("Please enter a non-negative integer")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    result = calculate_factorial(n)
    print(f"\nThe factorial of {n} is: {result}")

if __name__ == "__main__":
    main()