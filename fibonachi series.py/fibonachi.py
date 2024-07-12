def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series[:n]

result = generate_fibonacci(15)
print(result)
