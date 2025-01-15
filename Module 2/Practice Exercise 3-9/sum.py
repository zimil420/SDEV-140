# Initialize theSum to 0 and count to 0
theSum = 0
count = 0

# Start an infinite loop to accept user input
while True:
    # Display prompt for the user to input a number
    number = input("Enter a number or press Enter to quit: ")
    
    # If the user presses Enter without input, break the loop
    if number == "":
        break
    
    # Convert the input number to a floating-point value and add to theSum
    theSum += float(number)
    
    # Increment count to keep track of the number of inputs
    count += 1

# After the loop, display the sum
print(f"The sum is {theSum}")

# If count is greater than 0, calculate and display the average
if count > 0:
    print(f"The average is {theSum / count}")
