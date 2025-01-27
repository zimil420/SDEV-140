# This function will take the input string, sum up all the digits, and return the sum
def sum_of_digits(number_string):
    total = 0  # Initialize the total to zero
    
    # Loop through each character in the string
    for char in number_string:
        # Convert each character to an integer and add it to the total
        total += int(char)
    
    return total  # Return the final sum of the digits

# Ask the user to enter a series of single-digit numbers
user_input = input("Enter a series of single-digit numbers: ")

# Call the function and display the result
result = sum_of_digits(user_input)
print("The sum of the digits is:", result)
