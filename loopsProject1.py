#task: Write a Python Program for Fibonacci numbers

def fibonacci(n):
    fib_seq = [0, 1]  # Initializing the sequence with the first two numbers
    for x in range(2, n):
        next_num = fib_seq[-1] + fib_seq[-2]  # Compute the next Fibonacci number
        fib_seq.append(next_num)
    return fib_seq

# Prompt the user for the number of Fibonacci numbers to generate
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)
