import random

# Function to generate random numbers and write them to a file
def generate_random_numbers(file_name, count):
    with open(file_name, 'w') as file:
        # Generate 'count' random numbers and write them to the file
        for _ in range(count):
            num = random.randint(1, 500)  # Generate a random number between 1 and 500
            file.write(f"{num}\n")  # Write the number to the file on a new line

# Function to read and display numbers from the file
def display_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = file.readlines()  # Read all lines from the file
        for num in numbers:
            print(num.strip())  # Print each number, removing the newline character

# Main program to ask for user input and execute the tasks
def main():
    # Ask the user how many random numbers they want
    count = int(input("Enter how many random numbers to generate: "))
    
    # Specify the file name to store the numbers
    file_name = "random_numbers.txt"
    
    # Generate random numbers and write them to the file
    generate_random_numbers(file_name, count)
    
    # Display the numbers to the console
    print("\nThe random numbers generated and stored in the file are:")
    display_numbers(file_name)

# Call the main function to execute the program
main()
