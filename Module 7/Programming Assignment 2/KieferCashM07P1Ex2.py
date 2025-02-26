"""
This module defines the Employee class and Production Worker subclass, with an example program in main to demonstrate

Author: Cash Kiefer
Updated on: 2/26/25
"""


# Define the Employee class
class Employee:
    def __init__(self, name, number):
        """Initialize Employee with name and number."""
        self.__name = name  # Private attribute for employee name
        self.__number = number  # Private attribute for employee number

    # Accessor (getter) methods
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Mutator (setter) methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

# Define the ProductionWorker class (subclass of Employee)
class ProductionWorker(Employee):
    def __init__(self, name, number, pay_rate, shift):
        """Initialize ProductionWorker with additional attributes."""
        super().__init__(name, number)  # Initialize parent class attributes
        self.__pay_rate = pay_rate  # Private attribute for hourly pay rate
        self.__shift = shift  # Private attribute for shift (1 for day, 2 for night)

    # Accessor (getter) methods
    def get_pay_rate(self):
        return self.__pay_rate

    def get_shift(self):
        return self.__shift

    # Mutator (setter) methods
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

# Main program
def main():
    # Get user input
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    pay_rate = float(input("Enter the hourly pay rate: "))
    
    # Get and validate shift input
    while True:
        shift = int(input("Enter shift number (1 for day, 2 for night): "))
        if shift in [1, 2]:
            break
        else:
            print("Invalid input. Please enter 1 for day shift or 2 for night shift.")

    # Create an object of ProductionWorker
    worker = ProductionWorker(name, number, pay_rate, shift)

    # Display stored information
    print("\nEmployee Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")

# Run the program
if __name__ == "__main__":
    main()

