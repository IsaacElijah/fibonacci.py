def fibonacci(n, memo={}):
    """Function to calculate the nth Fibonacci number using memoization"""
    if n in memo:
        return memo[n]
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]
  
def generate_fibonacci_sequence(n):
    """Generate the first n fibonacci numbers"""
    if n <= 0:
        return "Input must be a positive integer"

    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]  # Return the first n numbers of the sequence

def main():
    """Main function to interact with the user and generate a fibonacci sequence"""
    print()
    print("Hello, Welcome to the Fibonacci Sequence Generator!")
    print()

    while True:
        try:
            n = int(input("Please enter the number of Fibonacci numbers to generate: "))
            if n <= 0:
                print()
                print("Input must be a positive integer")
                print()
                continue
            break
        except ValueError:
            print()
            print("Invalid input. Please enter a positive integer.")
            print()

    sequence = generate_fibonacci_sequence(n)
    print(f"\nFibonacci Sequence of {n} terms: {sequence}")

if __name__ == "__main__":
    main()
