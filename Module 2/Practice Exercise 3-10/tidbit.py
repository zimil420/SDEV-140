# Constants for calculations
ANNUAL_RATE = 0.12  # Annual interest rate
MONTHLY_RATE = ANNUAL_RATE / 12  # Monthly interest rate
DOWNPAYMENT_RATE = 0.10  # Down payment percentage
TABLEFORMATSTRING = "{:<5}{:<17.2f}{:<17.2f}{:<17.2f}{:<17.2f}{:<17.2f}"

# Input: Get the purchase price from the user
purchase_price = float(input("Enter the purchase price: "))

# Calculate the initial values
monthly_payment = 0.05 * purchase_price  # Monthly payment is 5% of the purchase price
down_payment = purchase_price * DOWNPAYMENT_RATE  # Down payment amount
balance = purchase_price - down_payment  # Initial balance owed

# Output the table header
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

# Initialize the month counter
month = 1

# Loop until the balance is fully paid
while balance > 0:
    # Calculate interest for the current month
    interest = balance * MONTHLY_RATE

    # If the balance is less than the monthly payment, adjust the payment
    if monthly_payment > balance + interest:
        monthly_payment = balance + interest

    # Calculate the principal amount for this month
    principal = monthly_payment - interest

    # Calculate the remaining balance after payment
    remaining_balance = balance - principal

    # Display the payment details for the current month
    print(TABLEFORMATSTRING.format(
        month, balance, interest, principal, monthly_payment, remaining_balance
    ))

    # Update the balance and increment the month counter
    balance = remaining_balance
    month += 1
