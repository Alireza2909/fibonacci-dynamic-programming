# Fibonacci Sequence using Dynamic Programming in Python

def fibonacci(n):
    # Create an array to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    # Fill the array with Fibonacci numbers using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")