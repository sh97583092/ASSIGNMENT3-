def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = 10
fact = factorial(number)

print(f"The factorial of {number} is {fact}")

number = 0
fact = factorial(number)
print(f"The factorial of {number} is {fact}")

number = -1
fact = factorial(number)
print(f"The factorial of {number} is {fact}")