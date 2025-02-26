"""
This module defines a Person class and a Customer subclass.

The Person class stores basic personal information such as name, address, and phone number.
The Customer class extends the Person class to include customer-specific details such as
customer number and mailing list preference.

A demonstration of the Customer class is provided in the __main__ block.

Author: Cash Kiefer
Date: 2/26/25
"""

# Define the Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name  # Store the person's name
        self.address = address  # Store the person's address
        self.phone = phone  # Store the person's telephone number

    def display_info(self):
        """Displays the person's details."""
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"

# Define the Customer class as a subclass of Person
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)  # Call the constructor of the Person class
        self.customer_number = customer_number  # Store the customer number
        self.mailing_list = mailing_list  # Store mailing list preference (True/False)

    def display_customer_info(self):
        """Displays the customer's details, including mailing list preference."""
        mailing_status = "Yes" if self.mailing_list else "No"
        return f"{self.display_info()}\nCustomer Number: {self.customer_number}\nOn Mailing List: {mailing_status}"

# Demonstrate an instance of Customer
if __name__ == "__main__":
    # Create a Customer instance
    customer1 = Customer("John Doe", "123 Main St, Cityville", "555-1234", 1001, True)
    
    # Display the customer's information
    print(customer1.display_customer_info())
