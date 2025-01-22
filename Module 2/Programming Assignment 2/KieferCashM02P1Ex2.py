# Program to calculate the factorial of a nonnegative integer using a loop

def calculate_factorial(n):
    """
    This function calculates the factorial of a given nonnegative integer n.
    """
    factorial = 1  # Initialize the factorial to 1 (as 0! = 1 and 1! = 1)
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        factorial *= i  # Multiply the current value of factorial by i
    return factorial

# Prompt the user to enter a nonnegative integer
try:
    number = int(input("Enter a nonnegative integer: "))  # Convert input to an integer
    if number < 0:
        print("Error: You entered a negative number. Please enter a nonnegative integer.")
    else:
        # Calculate the factorial using the function
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
