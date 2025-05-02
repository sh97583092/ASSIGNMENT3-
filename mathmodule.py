import math

# Q 1.   Asks the user for a number as input.
number = float(input("Enter a number: "))

# Q 2.   Uses the math module to calculate the:
#o   Square root of the number
if number >= 0:
    square_root = math.sqrt(number)
    print("Square root:", square_root)
else:
    print("Cannot calculate the square root of a negative number.")

# o   Natural logarithm (log base e) of the number
if number > 0:
    natural_log = math.log(number)
    print("Natural logarithm (base e):", natural_log)
else:
    print("Cannot calculate the logarithm of zero or a negative number.")

# o   Sine of the number (in radians)
sine_value = math.sin(number)
print("Sine (in radians):", sine_value)
