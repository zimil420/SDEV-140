def calculate_sales_tax():
    """
    This function prompts the user to enter total sales for the month, then calculates
    and displays the county sales tax, state sales tax, and total sales tax.
    """
    
    # Define sales tax rates
    STATE_TAX_RATE = 0.05  # 5% state tax
    COUNTY_TAX_RATE = 0.025  # 2.5% county tax

    # Get user input for total sales
    try:
        total_sales = float(input("Enter the total sales for the month: $"))
        
        if total_sales < 0:
            print("Total sales cannot be negative. Please enter a valid amount.")
            return
        
        # Calculate the taxes
        county_tax = total_sales * COUNTY_TAX_RATE
        state_tax = total_sales * STATE_TAX_RATE
        total_tax = county_tax + state_tax

        # Display results
        print("\nSales Tax Report:")
        print(f"Total Sales: ${total_sales:,.2f}")
        print(f"County Sales Tax (2.5%): ${county_tax:,.2f}")
        print(f"State Sales Tax (5%): ${state_tax:,.2f}")
        print(f"Total Sales Tax: ${total_tax:,.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the function
calculate_sales_tax()
