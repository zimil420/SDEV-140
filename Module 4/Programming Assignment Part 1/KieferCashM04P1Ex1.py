# Function to check if a number is prime
def is_prime(num):
    # A prime number is greater than 1 and divisible only by 1 and itself
    if num <= 1:
        return False
    for i in range(2, num):
        # If num is divisible by any number other than 1 and itself, it's not prime
        if num % i == 0:
            return False
    return True

# Main function to get user input and display prime numbers
def display_primes():
    # Ask the user to enter a number greater than 1
    number = int(input("Enter an integer greater than 1: "))
    
    # Create a list of integers from 2 up to the entered number
    numbers_list = list(range(2, number + 1))
    
    # Loop through each number in the list and check if it's prime
    for num in numbers_list:
        if is_prime(num):
            print(num)  # Display the prime number

# Call the main function
display_primes()
