Fibonacci = [0, 1]
n = 20  # Number of Fibonacci numbers to generate
for i in range(2, n): # Start from index 2
    next_fibnumber = Fibonacci[i - 1] + Fibonacci[i - 2] # Calculate the next Fibonacci number
    Fibonacci.append(next_fibnumber) # Append it to the list
print(Fibonacci) # Print the list of Fibonacci numbers


