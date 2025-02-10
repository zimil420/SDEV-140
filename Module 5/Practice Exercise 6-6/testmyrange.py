# Defining the myRange function
def myRange(start, stop=None, step=None):
    # Handle cases where stop and/or step are not provided
    if stop is None:
        stop = start  # If no stop is provided, use start as the stop
        start = 0  # Set start to 0 because it was not provided
    if step is None:
        step = 1  # Default step is 1 if not provided
    
    # Create an empty list to store the result
    result = []
    
    # Generate the list by counting up or down
    if step > 0:
        # Incremental case
        current = start
        while current < stop:
            result.append(current)
            current += step
    elif step < 0:
        # Decremental case
        current = start
        while current > stop:
            result.append(current)
            current += step  # subtracting step since it's negative
    
    return result


# Testing the function
print(myRange(10))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10))       # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myRange(1, 10, 2))    # [1, 3, 5, 7, 9]
